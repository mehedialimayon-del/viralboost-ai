from pathlib import Path
import re, subprocess, tempfile
root=Path(__file__).resolve().parent
for file in ['index.html','cloud.html']:
    html=(root/file).read_text()
    assert '<!doctype html>' in html.lower(),file
    ids=re.findall(r'id="([^"]+)"',html)
    assert len(ids)==len(set(ids)),f'Duplicate HTML IDs in {file}'
    refs=set(re.findall(r"\$\('([^']+)'\)",html))
    assert refs.issubset(set(ids)),f'Unknown IDs: {refs-set(ids)} in {file}'
    scripts=re.findall(r'<script[^>]*>(.*?)</script>',html,re.S|re.I)
    for script in scripts:
        if not script.strip():continue
        with tempfile.NamedTemporaryFile('w',suffix='.mjs') as tmp:
            tmp.write(script);tmp.flush()
            subprocess.run(['node','--check',tmp.name],check=True,capture_output=True)
    print(f'PASS: {file} — unique IDs, references, JavaScript syntax')
print('Static QA complete; browser E2E remains pending.')
