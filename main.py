from validare.validare_client import ValidareClient
from validare.validare_film import ValidareFilm
from infrastructura.repo_filme import RepoFilme
from infrastructura.repo_clienti import RepoClienti
from infrastructura.repo_inchirieri import RepoInchirieri
from business.service_filme import ServiceFilme
from business.service_clienti import ServiceClienti
from business.service_inchirieri import ServiceInchirieri
from prezentare.consola import Consola
from teste.teste import Teste
from infrastructura.repo_fisiere_clienti import FileRepoClienti
from infrastructura.repo_fisiere_filme import FileRepoFilme
from infrastructura.repo_inchirieri import FileRepoInchirieri

teste = Teste()
teste.run_all_tests()

validare_client = ValidareClient()
validare_film= ValidareFilm()

file_path1 = "C:\\Users\\A\\PycharmProjects\\Lab12\\infrastructura\\clienti.txt"
file_path2 = "C:\\Users\\A\\PycharmProjects\\Lab12\\infrastructura\\filme.txt"
file_path3 = "C:\\Users\\A\\PycharmProjects\\Lab12\\infrastructura\\inchirieri.txt"

repo_file_filme = FileRepoFilme(file_path2)
repo_file_clienti = FileRepoClienti(file_path1)
repo_file_inchirieri = FileRepoInchirieri(file_path3)

srv_clienti = ServiceClienti(repo_file_clienti,validare_client)
srv_filme = ServiceFilme(repo_file_filme,validare_film)
srv_inchirieri = ServiceInchirieri(repo_file_filme,repo_file_clienti,repo_file_inchirieri)

ui = Consola(srv_filme,srv_clienti,srv_inchirieri)
ui.run()

#repo_file_clienti._write_all_clienti_to_file()
#repo_file_filme.write_all_to_file_filme()

#stergere client -> stergere inchiriere cu id client
#arhivare proiect
#tot testat
#inchiriere de film/client inexistent
