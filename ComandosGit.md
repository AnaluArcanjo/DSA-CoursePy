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

#### renomeando a branch: </br>
     git checkout nome_do_branch

</br>

git pull </br>
git merge </br>
git push </br>

git checkout BRANCH_MAIN > git pull origin BRANCH_MAIN > git merge NAME_BRANCH > git push origin main

</br>

> ### Checagem de user:
    git config --global user.name
    git config --global user.email
    git show

</br></br> 

ls               -   checando o Repositório/Caminhos e Pastas </br>
git checkout     -   checando a Branch </br>
git show         -   mostra seu Usuário </br><br>








