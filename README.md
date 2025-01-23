## Setup GitHub

Pt a configura acest repository pe laptop-ul tau, creeaza un folder, care va contine fisierele, si deschide-l apoi cu Visual Studio Code.

Din Visual Studio Code, deschide terminalul integrat apasand **CTRL + \`**, si tasteaza urmatoarele comenzi:

`git init`
`git remote add origin <REPOSITORY_URL>`

, unde `<REPOSITORY_URL>` il poti obtine intrand pe GitHub pe pagina repository-ului, apasand butonul verde `<> CODE`, selectand HTTPS si copiind link-ul obtinut.

Apoi, dupa ce reusesti sa adaugi link-ul ca sursa remote cu succes, ruleaza:

`git pull origin master`

Si optional

`git pull origin master <DENUMIRE_BRANCH>`

pentru fiecare branch pe care doresti sa il ai si tu.

## Setup proiect

Imediat ce clonezi acest repository pe calculatorul tau, verifica daca ai Python instalat folosind:

`python --version`
`pip --version`

Daca nu il ai, instaleaza-l folosind site-ul oficial de la https://www.python.org/downloads/, si ai grija sa bifezi ca vrei sa adaugi Python in PATH! Apoi restarteaza calculatorul.

Daca totul e ok, ruleaza urmatoarea comanda, din directorul proiectului:

`pip install -r requirements.txt`

Asta va instala pachetele de care ai nevoie pentru a putea rula aplicatia. Dupa ce se termina de instalat acestea, verifica daca a functionat ruland:

`python main.py`

Asta ar trebui sa iti deschida fereastra aplicatiei (la inceput goala).

**WARNING:** Recomandabil este sa se ruleze comanda de instalare a dependentelor de mai sus ori de cate ori se cloneaza pe calculator o versiune mai noua a acestui repository, fiindca pachetele se mai pot schimba de la un update la altul.

## Lucrul cu GitHub

Daca ai clonat cu succes repository-ul pe calculatorul tau, incepe prin a rula:

`git branch`

Ar trebui sa vezi toate branch-urile pe care ti le-ai adaugat folosind comanda `pull`, iar branch-ul master ar trebui sa iasa in evidenta, indicand ca momentan folosesti acest branch.

**ATENTIE!** Nu da niciodata push la schimbari la care lucrezi direct pe branch-ul master. Acest lucru poate suprascrie munca unor colegi daca nu e facut cu grija!

Acceseaza-l pe cel al feature-ului la care vrei sa lucrezi folosind:

`git checkout <NUMELE_BRANCHULUI>`

Pentru a verifica daca ai reusit, mai ruleaza o data prima comanda, si ar trebui sa vezi branch-ul pe care esti iesind in evidenta.

Daca totul e ok, te poti apuca de treaba! :)

Dupa ce adaugi / modifici o parte de cod de care esti multumit, si care esti sigur ca functioneaza, este timpul sa o salvezi.

Mai intai, ruleaza:

`git status`

Aceasta comanda iti va arata ce schimbari s-au produs de la ultima salvare.

Apoi, ruleaza:

`git add <nume_fisier1> <nume_fisier2>`

cu numele fisierelor modificate pe care le-ai vazut la comanda anterioara si pe care vrei sa le salvezi.

Daca vrei sa le salvezi pe toate, poti scrie mai direct:

`git add .`

Acum, daca mai rulezi o data `git status`, vei vedea ca modificarile au fost adaugate in zona de staging. Asta inseamna ca sunt gata sa fie salvate.

Pentru a le salva, trebuie sa creezi un commit nou. Poti face asta folosind comanda de mai jos, si adaugand un mesaj scurt, dar descriptiv, despre ce schimbari aduce commit-ul:

`git commit -m "<Un mesaj despre schimbarile aduse de commit>"`

PS: Mesajul trebuie scris intre " ".

Daca comanda este realizata cu succes, acum poti da push pe branch modificarilor, folosind comanda:

`git push origin <NUMELE_BRANCH-ULUI>`

Commanda `commit` salveaza doar local schimbarile. Comanda `push` incarca aceste schimbari si in repository-ul GitHub de pe internet, unde le pot vedea si ceilalti membri.

Atunci cand un branch e gata, trebuie facut un pull request, pentru ca tot ce e scris pe branch sa se imbine cu codul principal din master. Despre asta vom vorbi la timpul potrivit.

### Reguli:
- **Nu da niciodata _push_ direct pe master!!**
- Nu sterge niciodata fisierul .gitignore.
- Nu sterge niciodata fisierul .git.
- Nu adauga fisiere noi in .gitignore fara sa te consulti cu restul echipei.
- Nu modifica folder-ul _\_\_pycache\_\__ din proiect (acesta va aparea dupa instalarea pachetelor).