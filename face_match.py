# -*- coding: iso-8859-1 -*-

import face_recognition as fr
import os

def compare(path1, path2):

    faces1 = fr.face_encodings(
        fr.load_image_file(path1))
    try:
        if len(faces1) == 1:
            faces2 = fr.face_encodings(
                fr.load_image_file(path2))

            if len(faces2) == 1:
                for face1 in faces1:
                    results = fr.compare_faces([face1], faces2[0], tolerance=0.5)
                    result = results[0]

                    if result:
                        os.system("clear")
                        return ("Mesma pessoa")
                    else:
                        os.system("clear")
                        return("Pessoas diferentes")

            elif len(faces2) > 1:
                os.system("clear")
                return "Mais de um rosto encontrado na segunda imagem."

            else:
                os.system("clear")
                return "Nenhum rosto encontrado na segunda imagem."

        elif len(faces1) > 1:
            os.system("clear")
            return "Mais de um rosto encontrado na primeira imagem."
        else:
            os.system("clear")
            return "Nenhum rosto encontrado na primeira imagem."
        
    except FileNotFoundError:
        os.system("clear")
        return "Arquivo não encontrado ou extensão errada"