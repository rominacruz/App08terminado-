import flet as ft


def main(page: ft.Page):
#establecer el tamaño  de la pantalla 
    page.window_width=800
    page.window_height=800
    
    page.bgcolor="black"
    page.title="Mictlan"
    page.ftcolor="gray"
    
    
#Audios 
    Intro=ft.Audio(src="Intro.mp3",volumen=1,balance=0)
    page.overlay.append(Intro)
    
    Nivel1=ft.Audio(src="Primer_Nivel.mp3",volumen=1,balance=0)
    page.overlay.append(Nivel1)
    
    Nivel2=ft.Audio(src="Segundo_Nivel.mp3",volumen=1,balance=0)
    page.overlay.append(Nivel2)
    
    Nivel3=ft.Audio(src="Tercer_Nivel.mp3",volumen=1,balance=0)
    page.overlay.append(Nivel3)
    
    Nivel4=ft.Audio(src="Cuarto_Nivel.mp3",volumen=1,balance=0)
    page.overlay.append(Nivel4)
    
    Nivel5=ft.Audio(src="Quinto_Nivel.mp3",volumen=1,balance=0)
    page.overlay.append(Nivel5)
    
    Nivel6=ft.Audio(src="Sexto_Nivel.mp3",volumen=1,balance=0)
    page.overlay.append(Nivel6)
    
    Nivel7=ft.Audio(src="Septimo_Nivel.mp3",volumen=1,balance=0)
    page.overlay.append(Nivel7)
    
    Nivel8=ft.Audio(src="Octavo_Nivel.mp3",volumen=1,balance=0)
    page.overlay.append(Nivel8)
    
    Nivel9=ft.Audio(src="Noveno_Nivel.mp3",volumen=1,balance=0)
    page.overlay.append(Nivel9)
    
#creamos interfaz 
Se crea la interfaz 
    btnIntro=ft.FilledButton(text="Escucha el Intro",disabled=False,on_click=lambda e:playintro(e))
    
    btnNivel1=ft.ElevatedButton(text="Primer nivel",on_click=lambda e:play1(e))
    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)
    
    btnNivel2=ft.ElevatedButton(text="Segundo nivel",on_click=lambda e:play2(e))
    img2=ft.Image(src="segundo-Nivel.jpeg",width=150,height=150)
    
    btnNivel3=ft.ElevatedButton(text="Tercer nivel",on_click=lambda e:play3(e))
    img3=ft.Image(src="Tercer-Nivel.png",width=150,height=150)
    
    btnNivel4=ft.ElevatedButton(text="Cuarto nivel",on_click=lambda e:play4(e))
    img4=ft.Image(src="Cuarto-Nivel.jpeg",width=150,height=150)
    
    btnNivel5=ft.ElevatedButton(text="Quinto nivel",on_click=lambda e:play5(e))
    img5=ft.Image(src="Quinto-Nivel.jpeg",width=150,height=150)
    
    btnNivel6=ft.ElevatedButton(text="Sexto nivel",on_click=lambda e:play6(e))
    img6=ft.Image(src="Sexto-Nivel.jpeg",width=150,height=150)
    
    btnNivel7=ft.ElevatedButton(text="Septimo nivel",on_click=lambda e:play7(e))
    img7=ft.Image(src="Septimo-Nivel.jpeg",width=150,height=150)
    
    btnNivel8=ft.ElevatedButton(text="Octavo nivel",on_click=lambda e:play8(e))
    img8=ft.Image(src="Octavo-Nivel.png",width=150,height=150)
    
    btnNivel9=ft.ElevatedButton(text="Noveno nivel",on_click=lambda e:play9(e))
    img9=ft.Image(src="Noveno-Nivel.jpeg",width=150,height=150)
    
    page.add(
        ft.Row(
            alignment="start",
            controls=[btnIntro]
            ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=[
                    
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel1,img1]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel2,img2]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel3,img3]
                            ),
                        ]
                    )
                ]
            ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=[
                    
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel4,img4]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel5,img5]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel6,img6]
                            ),
                        ]
                    )
                ]
            ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=[
                    
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel7,img7]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel8,img8]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel9,img9]
                            ),
                        ]
                    )
                ]
            ),
    )
    
    
    
    
    
    
    
    