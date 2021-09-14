import asyncio
import json
import callofduty
from callofduty import *
from PySimpleGUI import PySimpleGUI as sg 


async def main():
    client = await callofduty.Login()
    friends = await get_players(client)
    
async def get_players(client):
    players=['Stabilocócos#7181069', 'xXHenlolXx','Jaison_BR#4617106']
    #'Infantry#2974825','Neblina#5169134','Destruidor#8839422','Moneisson#3629808','Mohamed#7718250','Kami#8537689','Alves#2635821','Aynz#2635821','lufy#2715203']
    kdlist=[]
    jogadores={}
    
    adam = await client.GetPlayer(Platform.Activision, 'xXHenlolXx')
    adamprofile = await adam.profile(Title.ModernWarfare, Mode.Warzone)
    print(adamprofile["weekly"]["mode"]["br_all"]["properties"]["kdRatio"])
    with open("henloooool.txt", "w") as f:
        json.dump(adamprofile,f,ensure_ascii=False, indent=4)
    
    
    for player in players:
        x=await client.GetPlayer(Platform.Activision, player)
        try:
            profile= await x.profile(Title.ModernWarfare, Mode.Warzone)
        except:
            print("Perfil privado")
            #players.pop(players.index(player))
        else:
            kdlist.append(profile["weekly"]["mode"]["br_all"]["properties"]["kdRatio"])
            print(kdlist) 
        
    for player in players:
        jogadores[player]=kdlist[players.index(player)]
        
    print(jogadores)
    
    dict(sorted(jogadores.items(), key=lambda item: item[1]))
    
    layout=[
        [sg.Text("KD Semanal"), sg.Text("Jogadores")]
    ]
    
    for kd in kdlist:
        print(str(kd) + " " + players[kdlist.index(kd)])
        layout=layout + [[sg.Text(kd), sg.Text(players[kdlist.index(kd)])]]        
    sg.theme('Reddit')
        
    janela=sg.Window('Bala de Prata', layout)
    
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
    
    return 0 
    

asyncio.get_event_loop().run_until_complete(main())
