from IPython.display import Image as IPyImage, Markdown as md, display
import matplotlib.pyplot as plt
from PIL import Image

escolhas = ""

display(md('#AUmigos da vizinhança'))
display(md('##Adote aqui'))

# Exibindo a imagem em uma linha
plt.imshow(Image.open('/content/aumigo da vizinhança.jpeg'))
plt.axis('off')
plt.show()

display(md('###Antes de continuar, é necessário que você leia e aceite nossos Termos de Serviço. Deseja prosseguir e aceitar os termos?'))
print('''[1] Sim
[2] Não''')

option = str(input('Sua escolha é: '))
while option != '1':
    print('Tente novamente')
    option = str(input('Sua escolha é: '))
escolhas += str(option)

if option == '1':
        print('Você aceitou os termos')
elif option == '2':
        print('Você não aceitou os termos')

display(md('''###Porte'''))
print('''[1] Pequeno
[2] Médio
[3] Grande''')

option = str(input('Sua escolha é: '))
while option != '1' and option != '2' and option != '3':
    print('Tente novamente')
    option = str(input('Sua escolha é: '))
escolhas += str(option)

if option == '1':
        print('Pequenos foram selecionados')
elif option == '2':
        print('Médios foram selecionados')
elif option == '3':
        print('Grandes foram selecionados')

display(md('''###Sexo'''))
print('''[1] Macho
[2] Fêmea''')

option = str(input('Sua escolha é: '))
while option != '1' and option != '2':
    print('Tente novamente')
    option = str(input('Sua escolha é: '))
escolhas += str(option)

if option == '1':
        print('Machos foram selecionados')
elif option == '2':
        print('Fêmeas foram selecionadas')

display(md('''###Idade'''))
print('''[1] Filhote
[2] Adulto
[3]Sênior''')

option = str(input('Sua escolha é: '))
while option != '1' and option != '2' and option != '3':
    print('Tente novamente')
    option = str(input('Sua escolha é: '))
escolhas += str(option)

if option == '1':
        print('Filhotes foram selecionados')
elif option == '2':
        print('Adultos foram selecionados')
elif option == '3':
        print('Seniores foram selecionados')

display(md('''###Raça'''))
print('''[1] Vira-lata
[2] Com pedigree  ''')

option = str(input('Sua escolha é: '))
while option != '1' and option != '2':
    print('Tente novamente')
    option = str(input('Sua escolha é: '))
escolhas += str(option)

if option == '1':
        print('Vira-latas foram selecionados')
elif option == '2':
        print('Com pedigree foram selecionados')

display(md('''###A distância da loja de adoção até sua residência pode ser: '''))
print('''[1] Até 20km
[2] Além de 20km''')

option = str(input('Sua escolha é: '))
while option != '1' and option != '2':
    print('Tente novamente')
    option = str(input('Sua escolha é: '))
escolhas += str(option)

if option == '1':
        print('Até 20km foram selecionados')
elif option == '2':
        print('Além de 20km foram selecionados')

display(md('####Muito obrigado por nos fornecer suas especificações, deseja prosseguir?'))
print('''[1] Sim
[2] Não''')

option = str(input('Sua escolha é: '))
while option != '1':
    print('Tente novamente')
    option = str(input('Sua escolha é: '))
escolhas += str(option)

display(md('##Você aceita este adorável companheiro como seu novo AUmigo'))

if escolhas.startswith("1111111"): # 1. Pequeno - Macho - Filhote - Vira-lata - Até 20km
    display(IPyImage(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREUCLpNPfx3eWMhwloG_g9axy7FU_xmMg7hQ&s"))
    display(md('Ricardo'))

elif escolhas.startswith('1111121'): # 2. Pequeno - Macho - Filhote - Vira-lata - Além de 20km
    display(IPyImage(url='https://i.pinimg.com/736x/bd/ac/86/bdac86a7e433bac61c7cbf6d49067091.jpg'))
    display(md('Neymar'))

elif escolhas.startswith("1111211"): # 3. Pequeno - Macho - Filhote - Com pedigree - Até 20km
    display(IPyImage(url='https://www.petz.com.br/blog/wp-content/uploads/2018/06/cachorros-pequenos.jpg'))
    display(md('Lucas'))

elif escolhas.startswith("1111221"): # 4. Pequeno - Macho - Filhote - Com pedigree - Além de 20km
    display(IPyImage(url='https://img.myloview.com.br/quadros/filhote-de-cachorro-engracado-da-chihuahua-levanta-em-um-fundo-branco-700-18542628.jpg'))
    display(md('Dudão'))

elif escolhas.startswith("1112111"): # 5. Pequeno - Macho - Adulto - Vira-lata - Até 20km
    display(IPyImage(url="https://blog-static.petlove.com.br/wp-content/uploads/2020/06/chihuahua-bravo-petlove.jpg"))
    display(md('Barnabé'))

elif escolhas.startswith('1112121'): # 6. Pequeno - Macho - Adulto - Vira-lata - Além de 20km
    display(IPyImage(url='https://i.pinimg.com/236x/29/02/f2/2902f2849cd515dafe9dee50d0765cdb.jpg'))
    display(md('Nino'))

elif escolhas.startswith('1112211'): # 7. Pequeno - Macho - Adulto - Com pedigree - Até 20km
    display(IPyImage(url='https://i.pinimg.com/236x/15/b2/dc/15b2dcde1028834ee178b60df9a007c2.jpg'))
    display(md('Salsicha'))

elif escolhas.startswith("1112221"): # 8. Pequeno - Macho - Adulto - Com pedigree - Além de 20km
    display(IPyImage(url='https://previews.123rf.com/images/kvkirillov/kvkirillov2302/kvkirillov230200031/199355077-filhote-de-cachorro-engra%C3%A7ado-sozinho-yorkshire-terrier-com-retrato-de-rosto-divertido.jpg'))
    display(md('Gucci'))

elif escolhas.startswith("1113111"): # 9. Pequeno - Macho - Sênior - Vira-lata - Até 20km
    display(IPyImage(url='https://s2-glamour.glbimg.com/zv9Giu26ZNgHbs3O1eu5fuI8RFc=/0x0:607x426/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_ba3db981e6d14e54bb84be31c923b00c/internal_photos/bs/2021/x/L/vNU8n5S3icJhszkvj8QQ/2020-02-27-vira-lata.jpg'))
    display(md('Rosimã'))

elif escolhas.startswith('1113121'): # 10. Pequeno - Macho - Sênior - Vira-lata - Além de 20km
    display(IPyImage(url='https://chefbob.com.br/wp-content/uploads/2020/01/2020-01-22-racas-de-caes.jpg'))
    display(md('Mask'))

elif escolhas.startswith('1113211'): # 11. Pequeno - Macho - Sênior - Com pedigree - Até 20km
    display(IPyImage(url='https://png.pngtree.com/png-vector/20231115/ourlarge/pngtree-brittany-spaniel-senior-png-image_10609432.png'))
    display(md('Bello'))

elif escolhas.startswith('1113221'): # 12. Pequeno - Macho - Sênior - Com pedigree - Além de 20
    display(IPyImage(url='https://fofuxo.com.br/_upload/content/2014/07/04/schnauzer.jpg'))
    display(md('Lucas'))

elif escolhas.startswith("1121111"): # 13. Pequeno - Fêmea - Filhote - Vira-lata - Até 20km
    display(IPyImage(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTacVu1znpnkGwkJGHA-WdX397kEepir6pkMg&s"))
    display(md('Meggy'))

elif escolhas.startswith("1121121"): # 14. Pequeno - Fêmea - Filhote - Vira-lata - Além de 20km
    display(IPyImage(url="https://fotos.amomeupet.org/uploads/fotos/1735065562_676affda13074_hd.jpg"))
    display(md('Dyaa'))

elif escolhas.startswith("1121211"): # 15. Pequeno - Fêmea - Filhote - Com pedigree - Até 20km
    display(IPyImage(url="https://cobasiblog.blob.core.windows.net/production-ofc/2021/05/AdobeStock_181271379.webp"))
    display(md('Rose'))

elif escolhas.startswith("1121221"): # 16. Pequeno - Fêmea - Filhote - Com pedigree - Além de 20km
    display(IPyImage(url="https://www.patasdacasa.com.br/sites/default/files/styles/article_detail_1200/public/noticias/2022/01/preco-das-racas-de-cachorro-mais-populares.jpg.webp?itok=a-UYVJMd"))
    display(md('Tiffany, Brittany, Megan ou Heather'))

elif escolhas.startswith("1122111"): # 17. Pequeno - Fêmea - Adulto - Vira-lata - Até 20km
    display(IPyImage(url="https://upload.wikimedia.org/wikipedia/commons/7/70/Serena_REFON.jpg"))
    display(md('Poppy'))

elif escolhas.startswith("1122121"): # 18. Pequeno - Fêmea - Adulto - Vira-lata - Além de 20km
    display(IPyImage(url="https://cdn0.umcomo.com.br/pt/posts/3/6/7/parar_de_cavar_o_seu_jardim_27763_2_600.jpg"))
    display(md('Pandora'))

elif escolhas.startswith("1122211"): # 19. Pequeno - Fêmea - Adulto - Com pedigree - Até 20km
    display(IPyImage(url="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_1200,h_675/https://vedovatipisos.com.br/wp-content/uploads/2015/12/ra%C3%A7as-de-cachorro-1200x675.jpg"))
    display(md('Joy ou Jassie'))

elif escolhas.startswith("1122221"): # 20. Pequeno - Fêmea - Adulto - Com pedigree - Além de 20km
    display(IPyImage(url="https://encrenquinhas.com.br/images/004.jpg"))
    display(md('Bettanie'))

elif escolhas.startswith("1123111"): # 21. Pequeno - Fêmea - Sênior - Vira-lata - Até 20km
    display(IPyImage(url="https://blog-static.petlove.com.br/wp-content/uploads/2021/07/cachorro-velho-pequeno-petlove.jpg"))
    display(md('Elsa'))

elif escolhas.startswith("1123121"): # 22. Pequeno - Fêmea - Sênior - Vira-lata - Além de 20km
    display(IPyImage(url="https://www.portaldodog.com.br/wp-content/uploads/2024/11/Sinais-de-cachorro-idoso.jpg"))
    display(md('Piper'))

elif escolhas.startswith("1123211"): # 23. Pequeno - Fêmea - Sênior - Com pedigree - Até 20km
    display(IPyImage(url="https://www.ourofinopet.com//media/uploads/blog/imagem/2023/20230731155853.jpg.400x400_q85_box-51%2C0%2C464%2C414_crop_detail.jpg"))
    display(md('Benta'))

elif escolhas.startswith("1123221"): # 24. Pequeno - Fêmea - Sênior - Com pedigree - Além de 20km
    display(IPyImage(url="https://adimax.com.br/wp-content/uploads/2022/08/racao-para-cachorro-idoso-formula-natural.jpg"))
    display(md('Peninha'))

elif escolhas.startswith("1211111"): # 25. Médio - Macho - Filhote - Vira-lata - Até 20km
    display(IPyImage(url="https://www.petz.com.br/blog/wp-content/uploads/2020/01/vira-lata-caramelo-cao.jpg" ))
    display(md('Tobi'))

elif escolhas.startswith("1211121"): # 26. Médio - Macho - Filhote - Vira-lata - Além de 20km
    display(IPyImage(url="https://www.patasdacasa.com.br/sites/default/files/styles/article_detail_1200/public/noticias/2022/03/filhote-de-vira-lata-da-gestacao-ao-adestramento-tudo-que-voce-precisa-saber-sobre-os-caezinhos-srd_1.jpg.webp?itok=BND7JJgB"))
    display(md('Biscoito'))

elif escolhas.startswith("1211211"): # 27. Médio - Macho - Filhote - Com pedigree - Até 20km
    display(IPyImage(url="https://purina.com.br/sites/default/files/2024-08/racas-cachorros-porte-medio-beagle-br.jpg"))
    display(md('Thor'))

elif escolhas.startswith("1211221"): # 28. Médio - Macho - Filhote - Com pedigree - Além de 20km
    display(IPyImage(url="https://www.petz.com.br/blog/wp-content/uploads/2022/10/nome-para-cachorro-blue-heeler3.jpg"))
    display(md('Trovão'))

elif escolhas.startswith("1212111"): # 29. Médio - Macho - Adulto - Vira-lata - Até 20km
    display(IPyImage(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5OjPcHb8LC8Galcst9meinD0-qbAuLZHekw&s"))
    display(md('Notridame'))

elif escolhas.startswith("1212121"): # 30. Médio - Macho - Adulto - Vira-lata - Além de 20km
    display(IPyImage(url="https://www.patasdacasa.com.br/sites/default/files/styles/article_detail_1200/public/noticias/2023/01/vira-lata-marrom-veja-galeria-com-fotos-desse-adoravel-caozinho.jpg.webp?itok=SfQYswJg"))
    display(md('Amendoim'))

elif escolhas.startswith("1212211"): # 31. Médio - Macho - Adulto - Com pedigree - Até 20km
    display(IPyImage(url="https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2023/02/27/443280990-border-collie.jpg"))
    display(md('Chico'))

elif escolhas.startswith("1212221"): # 32. Médio - Macho - Adulto - Com pedigree - Além de 20km
    display(IPyImage(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1UFXbz8Y52g9W2sJFFg-LvYjhpGku-OGHiw&s"))
    display(md('Marley'))

elif escolhas.startswith("1213111"): # 33. Médio - Macho - Sênior - Vira-lata - Até 20km
    display(IPyImage(url="https://cdn-imgs.s3.sa-east-1.amazonaws.com/wp-content/uploads/2025/01/cachorro-525x350.jpg"))
    display(md('Pingo'))

elif escolhas.startswith("1213121"): # 34. Médio - Macho - Sênior - Vira-lata - Além de 20km
    display(IPyImage(url="https://bompracachorro.blogfolha.uol.com.br/files/2021/10/7E991F1A-0E54-4924-A8B0-E7EB7F0A3593.jpeg"))
    display(md('Bob'))

elif escolhas.startswith("1213211"): # 35. Médio - Macho - Sênior - Com pedigree - Até 20km
    display(IPyImage(url="https://www.patasdacasa.com.br/sites/default/files/noticias/2022/04/cachorro-idoso-tudo-sobre-a-terceira-idade-dos-caes.png"))
    display(md('Zeus'))

elif escolhas.startswith("1213221"): # 36. Médio - Macho - Sênior - Com pedigree - Além de 20k
    display(IPyImage(url="https://img.freepik.com/fotos-premium/velho-buldogue-frances-grisalho-isolado-no-branco_191971-29800.jpg"))
    display(md('Loki'))

elif escolhas.startswith("1221111"): # 37. Médio - Macho - Filhote - Sem pedigree - Até 20 km
    display(IPyImage(url="https://br.pinterest.com/pin/267119821623862949/"))
    display(md('Luke'))

elif escolhas.startswith("1221121"): #38. Grande - Fêmea - Sênior - Com pedigree - Até 20 km
    display(IPyImage(url="https://blog-static.petlove.com.br/wp-content/uploads/2018/05/labradora-femea.jpg?_gl=1*1j8shtq*_gcl_au*MjEwMzEwMjUwOC4xNzQ2MTQyNDQ2"))
    display(md('Leia'))

elif escolhas.startswith("1221211"): #39. Grande - Macho - Filhote - Com pedigree - Além de 20 km
    display(IPyImage(url="url=https://cobasi.vteximg.com.br/arquivos/ids/726232/sao-bernardo-filhote.png?v=637590400198530000"))
    display(md('Scooby'))

elif escolhas.startswith("1221221"): #40. Pequeno - Fêmea - Filhote - Sem pedigree - Além de 20 km
    display(IPyImage(url="https://i.pinimg.com/736x/81/49/61/8149615949a35795ac960934f17ff059.jpg"))
    display(md('Liza'))

elif escolhas.startswith("1222111"): #41. Médio - Macho - Sênior - Com Pedigree - Até 20 km
    display(IPyImage(url="https://www.zooplus.pt/magazine/wp-content/uploads/2018/06/beagle_1.jpeg"))
    display(md('Coragem'))

elif escolhas.startswith("1222121"): #42. Pequeno - Macho - Sênior - Com Pedigree - Até 20 km
    display(IPyImage(url="https://www.zooplus.pt/magazine/wp-content/uploads/2017/03/schwarz-chihuahua-1024x683.jpg"))
    display(md('Adam'))

elif escolhas.startswith("1222211"): #43. Grande - Macho - Sênior - Com Pedigree - Até 20 km
    display(IPyImage(url="https://static.wixstatic.com/media/9fc6ef_4efab996f1794abd93aec17b8e79168d~mv2.jpg/v1/fill/w_740,h_599,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/9fc6ef_4efab996f1794abd93aec17b8e79168d~mv2.jpg"))
    display(md('Sandler'))

elif escolhas.startswith("1222221"): #44. Pequeno - Fêmea - Filhote - Com Pedigree - Além de 20 km
    display(IPyImage(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9WZrxgv-ztespmle8Dk4_B-Yk4mBDrIVLjg&s"))
    display(md('Angelina'))

elif escolhas.startswith("1223111"): #45. Grande - Fêmea - Filhote - Sem Pedigree - Até 20 km
    display(IPyImage(url="https://www.patasdacasa.com.br/sites/default/files/noticias/2021/06/cachorro-vira-lata-filhote-quais-os-cuidados-mais-importantes-durante-essa-fase.jpg"))
    display(md('Julie'))

elif escolhas.startswith("1223121"): #46. Grande - Macho - Sênior - Com Pedigree - Até 20 km
    display(IPyImage(url="https://veterinarioalphaconde.com.br/wp-content/uploads/2021/12/pastor-alemao-conheca-algumas-curiosidades-sobre-a-raca.jpg"))
    display(md('Jhony'))

elif escolhas.startswith("1223211"): #47. Grande - Macho - Filhote - Com Pedigree - Alèm de 20 km
    display(IPyImage(url="https://blog-static.petlove.com.br/wp-content/uploads/2019/08/shutterstock_630679700.jpg"))
    display(md('Legolas'))

elif escolhas.startswith("1223221"): #48. Médio - Fêmea - Sênior - Sem Pedigree - Até 20 km
    display(IPyImage(url="https://www.petz.com.br/blog/wp-content/uploads/2022/01/cruzamento-de-border-collie-com-vira-lata-interna.jpg"))
    display(md('Lessie'))

elif escolhas.startswith("1311111"):  # 49. Grande - Macho - Filhote - Vira-lata - Até 20km
    display(IPyImage(url="https://www.petz.com.br/blog/wp-content/uploads/2022/03/vira-lata-filhote.jpg"))
    display(md("Casca de bala"))

elif escolhas.startswith("1311121"):  # 50. Grande - Macho - Filhote - Vira-lata - Além de 20km
    display(IPyImage(url="https://cobasi.vteximg.com.br/arquivos/ids/723981/vira-lata-filhote.png?v=637588609420370000"))
    display(md("MC Kevin"))

elif escolhas.startswith("1311211"):  # 51. Grande - Macho - Filhote - Com pedigree - Até 20km
    display(IPyImage(url="https://img.olx.com.br/images/36/369538150664850.jpg"))
    display(md("Manoel gomes"))

elif escolhas.startswith("1311221"):  # 52. Grande - Macho - Filhote - Com pedigree - Além de 20km
    display(IPyImage(url="https://www.cotanet.com.br/img/site/paginas/venda-de-filhotes-de-grande-porte-com-pedigree.jpg"))
    display(md("Monark"))

elif escolhas.startswith("1312111"):  # 53. Grande - Macho - Adulto - Vira-lata - Até 20km
    display(IPyImage(url="https://s2-g1.glbimg.com/TdPTg4jg3ZqtmZtyFnuHehXLgmk=/0x314:720x1073/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/B/x/gU7r6UTvyFwLn5G5FlUg/whatsapp-image-2019-02-22-at-14.53.02.jpeg"))
    display(md("Orochinho"))

elif escolhas.startswith("1312121"):  # 54. Grande - Macho - Adulto - Vira-lata - Além de 20km
    display(IPyImage(url="https://live.staticflickr.com/3788/9097824098_52a8466a07_b.jpg"))
    display(md("Herobrine"))

elif escolhas.startswith("1312211"):  # 55. Grande - Macho - Adulto - Com pedigree - Até 20km
    display(IPyImage(url="https://www.doglife.com.br/blog/assets/post/racas-cachorro-grande-5ec3ceb1190dad1466b4c60e/Ra%C3%A7as%20de%20cachorro%20grande-min.jpg"))
    display(md("Homem aranha"))

elif escolhas.startswith("1312221"):  # 56. Grande - Macho - Adulto - Com pedigree - Além de 20km
    display(IPyImage(url="https://portaledicase.com/wp-content/uploads/2023/03/Labrador-retriever-1024x683.jpg"))
    display(md("Magneto"))

elif escolhas.startswith("1313111"):  # 57. Grande - Macho - Sênior - Vira-lata - Até 20km
    display(IPyImage(url="https://www.pedigree.com.br/sites/g/files/fnmzdf2401/files/2024-12/vira-lata-caramelo.jpg"))
    display(md("Fábio galileo"))

elif escolhas.startswith("1313121"):  # 58. Grande - Macho - Sênior - Vira-lata - Além de 20km
    display(IPyImage(url="https://cachorrosderaca.com.br/wp-content/uploads/2017/01/vira-lata.jpg"))
    display(md("Protagonista"))

elif escolhas.startswith("1313211"):  # 59. Grande - Macho - Sênior - Com pedigree - Até 20km
    display(IPyImage(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTJS9MJu2P1QKSmIPY03IcU-WbA7Vy7ml6jg&s"))
    display(md("Luva de ração"))

elif escolhas.startswith("1313221"):  # 60. Grande - Macho - Sênior - Com pedigree - Além de 20km
    display(IPyImage(url="https://www.petz.com.br/blog/wp-content/uploads/2020/03/maior-cao-do-mundo.jpg"))
    display(md("Bolt"))

elif escolhas.startswith('1321111'): #61. Grande - Fêmea - Filhote - Vira-lata - Até 20km
    display(IPyImage(url='https://www.patasdacasa.com.br/sites/default/files/noticias/2022/03/filhote-de-vira-lata-da-gestacao-ao-adestramento-tudo-que-voce-precisa-saber-sobre-os-caezinhos-srd_1.jpg'))
    display(md('Biscoito'))

elif escolhas.startswith('1321121'): #62. Grande - Fêmea - Filhote - Vira-lata - Além de 20km
    display(IPyImage(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDyaQOhPnnaC_joFgLMOT2kjJnrVX4-ei4Yg&s'))
    display(md('Amendoim'))

elif escolhas.startswith('1321211'): #63. Grande - Fêmea - Filhote - Com pedigree - Até 20km
    display(IPyImage(url='https://i.pinimg.com/236x/ae/b4/76/aeb476c26159ea44c62b08da0492d876.jpg'))
    display(md('Rachel'))

elif escolhas.startswith('1321221'): #64. Grande - Fêmea - Filhote - Com pedigree - Além de 20km
    display(IPyImage(url='https://canecorsobrasil.com.br/wp-content/uploads/2023/07/Cane-corso-brasil-rosto-close.webp'))
    display(md('Lola'))

elif escolhas.startswith('1322111'): #65. Grande - Fêmea - Adulto - Vira-lata - Até 20km
    display(IPyImage(url='https://conteudo.imguol.com.br/c/noticias/43/2021/04/23/vira-lata-mylo-que-e-cruzamento-das-racas-terra-nova-e-poodle-e-comparado-ao-personagem-chewbacca-de-star-wars-1619203008588_v2_1x1.jpg'))
    display(md('Manchas'))

elif escolhas.startswith('1322121'): #66. Grande - Fêmea - Adulto - Vira-lata - Além de 20km
    display(IPyImage(url='https://newr7-r7-prod.web.arc-cdn.net/resizer/v2/FZOA6T2WOJP4ROPOZLMGA5IHII.jpg?auth=d81beb257bb3eb8cbc428599a197bbff3f4575aae2a32e71bd233b081e0d9d99&width=772&height=421'))
    display(md('Bianca'))

elif escolhas.startswith('1322211'): #67. Grande - Fêmea - Adulto - Com pedigree - Até 20km
    display(IPyImage(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiaad302QgFnpmULB1Zbm9_qF9kDU8dXJT6A&s'))
    display(md('Bela'))

elif escolhas.startswith('1322221'): #68. Grande - Fêmea - Adulto - Com pedigree - Além de 20km
    display(IPyImage(url='https://www.petz.com.br/blog/wp-content/uploads/2020/04/pitbull-personalidade-caes.jpg'))
    display(md('Belinha'))

elif escolhas.startswith('1323111'): #69. Grande - Fêmea - Sênior - Vira-lata - Até 20km
    display(IPyImage(url='https://thumbs.dreamstime.com/b/mongrel-com-um-chap%C3%A9u-vermelho-aconchegante-relaxando-num-dia-de-inverno-ao-ar-livre-este-charmoso-monstro-adorava-branco-e-369001679.jpg'))
    display(md('Patrícia'))

elif escolhas.startswith('1323121'): #70. Grande - Fêmea - Sênior - Vira-lata - Além de 20km
    display(IPyImage(url='https://lh3.googleusercontent.com/proxy/wrDQQkFldZJOMaxVfuQJEvNKPncbOekRwvyl5YMje-QDzT5TjMDFMfNHLl5eI5VifMsihiTfV2ckcxf8gxm5swb87TB1NM2BJ7C-L8orIQ-E0obcURJxQx_GVUUWlTxL3pnsoMPzkKwamPy4D-fuhOyHSI7ifP9XQJwnCZ-Uix9h3ND4N2o3cZ6Of1SL'))
    display(md('Princesa'))

elif escolhas.startswith('1323211'): #71. Grande - Fêmea - Sênior - Com pedigree - Até 20km
    display(IPyImage(url='https://www.patasdacasa.com.br/sites/default/files/2024-03/sao-bernardo.jpg'))
    display(md('Bernarda'))

elif escolhas.startswith('1323221'): #72. Grande - Fêmea - Sênior - Com pedigree - Além de 20km
    display(IPyImage(url='https://fotos.amomeupet.org/uploads/fotos/1698191113_6538570946576_hd.jpeg'))
    display(md('Pandora'))
