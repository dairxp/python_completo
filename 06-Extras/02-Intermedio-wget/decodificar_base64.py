import base64
data="Codigo AQUI"

open("dni.jpg",'wb').write(base64.b64decode(data))