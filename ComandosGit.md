> ## Principais comandos Git - Repositório e Branch

> ### Criando um novo reposirório 
<!-- #### echo "# DSA-CoursePy" >> README.md -->
    git init
    git add README.md   
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/YOUR_USER_GIT/LINK_YOUR_REP.git
    git push -u origin main
</br></br> 

> ### Atualizando Repositório 
    git init
    git add . 
    git commit -m "commit_here"
    git push
</br></br> 

____________________________________________________ 
<!-- user now: AnaluArcanjo -->

> ### Trocando de Repositório
    ....
</br>

> ### Trocando Branch

#### fazendo checkout de uma branch existente: </br>  
    git checkout NOME-DA-BRANCH

#### fazendo checkout de uma nova branch: </br> 
    git checkout -b NOME-DA-NOVA-BRANCH

#### renomeando uma branch existente: </br>
     git branch -m NOME-DA-BRANCH    NOVO-NOME-DA-BRANCH

#### comitando branch existente: </br>
     git add NOME-ARQUIVO
     git git commit -m "Alterações locais no NOME-ARQUIVO.extensao"    

#### listando todas as branchs existentes: </br>
     git branch
     git branch -r      (branch remota)
     gti branch -a      (branch local + remota)

#### deletando uma branch existente: </br>
     git branch -d NOME-DA-BRANCH
     git branch -D a-       (executar esse comando, se o git reclamar que a branh n foi mesclada)



</br>

#### Passo-a-passo para atualizar a Branch principal (HEAD): </br>
    git checkout HEAD 
    <!-- git pull origin HEAD  -->
    git merge NAME_BRANCH 
    git push origin HEAD 

</br>

> ### Checagem de user:
    git config --global user.name
    git config --global user.email
    git show

</br></br> 

ls               -   checando o Repositório/Caminhos e Pastas </br>
git checkout     -   checando a Branch </br>
git show         -   mostra seu Usuário </br><br>








