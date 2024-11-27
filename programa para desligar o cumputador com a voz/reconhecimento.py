import speech_recognition as sr
import os

def ouvir_microfone():
    # Instancia o reconhecedor
    microfone = sr.Recognizer()

    while True:  # Loop contínuo para escutar comandos
        try:
            # Usa o microfone como fonte de áudio
            with sr.Microphone() as source:
                # Ajusta para ruídos no ambiente
                microfone.adjust_for_ambient_noise(source)
                print("Diga um comando:")

                # Escuta o áudio do usuário
                audio = microfone.listen(source)

                # Transcreve o áudio para texto
                frase = microfone.recognize_google(audio, language='pt-BR')
                print(f"Você disse: {frase}")

                # Comandos para abrir aplicativos
                if "desligar computador" in frase.lower():
                    print("Desligando o computador...")
                    os.system("shutdown /s /t 0")  # Desliga o computador (Windows)
                    break

                elif "abrir jogo" in frase.lower():
                    print("Abrindo o jogo osu!...")
                    os.system("C:\Users\freds\AppData\Local\osu!\osu!.exe")  # Substitua pelo caminho correto se necessário

                elif "abrir Excel" in frase.lower():
                    print("Abrindo o Excel...")
                    os.system('"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"')  # Substitua pelo caminho correto se necessário

                elif "parar" in frase.lower():
                    print("Encerrando o programa.")
                    break  # Sai do loop

                else:
                    print("Comando não reconhecido. Tente novamente.")

        except sr.UnknownValueError:
            # Caso o áudio não seja compreendido
            print("Não entendi o que você disse. Tente novamente.")
        except sr.RequestError:
            # Caso haja problemas de conexão ou serviço
            print("Erro ao tentar acessar o serviço de reconhecimento.")
            break  # Sai do loop em caso de erro crítico

# Chama a função para iniciar o reconhecimento contínuo
ouvir_microfone()
