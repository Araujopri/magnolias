segundos = (input("Por favor, entre com o número de segundos que deseja converter: "))
tot_segundos = int(segundos)
dias = tot_segundos // 86400
seg_restantes1 = tot_segundos%86400
horas = seg_restantes1 // 3600
seg_restantes2 = seg_restantes1 % 3600
minutos = seg_restantes2 // 60
seg_rest_final = seg_restantes2 % 60

print(dias, "dias,", horas, "horas,", minutos,"minutos e", seg_rest_final, "segundos.")
 
