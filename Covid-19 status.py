import subprocess
import sys
import time

print("Check the covid status of any country and also the global staus")
def install(package):
       subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def cases():
    
                import subprocess
                import sys
                import time
                from covid import Covid
                covid = Covid()
                answer = input('Would you like a list of all the countries (Y or N): ')
                
                if answer == 'Y' or answer == 'y':
                        print(covid.list_countries())
                
                Country = input('Enter Country to Get Covid Status: ')
                country = covid.get_status_by_country_name(Country)
                
                
                gactive = covid.get_total_active_cases()
                gconfirmed = covid.get_total_confirmed_cases()
                grecovered = covid.get_total_recovered()
                gdeaths = covid.get_total_deaths()
                data ={ 
                        key:country[key] 
                        for key in country.keys() and {'confirmed',  
                                                'active', 
                                                'deaths', 
                                                'recovered',
                                                'country'} 
                } 

                key = []
                value = []
                for i in data.keys():
                        key.append(i)
                for x in data.values():
                        value.append(str(x))


                confirmed = key[0] + ': ' + value[0]
                active = key[1] + ': ' + value[1]
                deaths = key[2] + ': ' + value[2]
                recovered = key[3] + ': ' + value[3]
                con = value[4]
                
                
                
                print("                             ")
                print(con + ': ')  
                print(confirmed)
                print(active)
                print(deaths)
                print(recovered)
                
                print('                                                       ')
                print('                                                       ')
                
                print("Global: ")
                print('Confirmed: ', end = '')
                print(gconfirmed)
                print('Active:: ', end = '')
                print(gactive)
                print('Deaths: ', end = '')
                print(gdeaths)
                print("Recovered: ", end = '')
                print(grecovered)
                print(Country)




try:
   cases()

except ModuleNotFoundError:
        print('You do not have the prerequisites installed')
        print('installing...')
        
        install('covid')
        
        for x in range(1,3):
                print('')
                time.sleep(1)
        print('Done...')
        for x in range(1,3):
                    print('')
                    time.sleep(1)
        
        cases()

except ValueError:
        print('Invalid Country,  check the list!')
        cases()