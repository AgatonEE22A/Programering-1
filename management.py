
datorer = ["Dator 1", "Dator 2", "Dator 3", "Dator 4", "Dator 5"]
service_datorer = []
datorer_pa_service = 0

while datorer_pa_service < 3:
    print("\nDatorer i företaget:")
    for i in range(len(datorer)):
        print(f"{i + 1}. {datorer[i]}")
        if datorer[i] not in service_datorer:  # Visa endast datorer som inte är på service
            print(f"{i + 1}. {datorer[i]}")
    
    print("\nDatorer på service:")
    for i in range(len(service_datorer)):
        print(f"{i + 1}. {service_datorer[i]}")
    
    try:
        val = int(input("\nVälj vilken dator du vill skicka på service (ange siffra): ")) - 1

        if 0 <= val < len(datorer):
            dator_till_service = datorer[val]
        if 0 <= val < len(datorer) and datorer[val] not in service_datorer:
            dator_till_service = datorer[val]  # Hämta den valda datorn
            service_datorer.append(dator_till_service)
            datorer.pop(val)
            datorer_pa_service += 1
            print(f"\n{dator_till_service} har skickats på service.")
        else:
            print("Ogiltigt val, försök igen.")
            print("Ogiltigt val eller datorn är redan på service, försök igen.")

    except ValueError:
        print("Ange en giltig siffra.")

print("\nTre datorer har skickats på service. Programmet avslutas.")
print("\nTre datorer har skickats på service. Programmet avslutas.")