import datetime
horaImp = datetime.datetime.now()
data = f"{horaImp.day:02d}/{horaImp.month:02d}/{horaImp.year:02d}"
hora = f"{horaImp.hour:02d}:{horaImp.minute:02d}"
print(f"Data: {data}")
print(f"Hora: {hora}")