import streamlit as st
import pandas as pd
import folium
import geopy
from geopy.geocoders import Nominatim
import datetime
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import st_folium

blog_post=st.sidebar.radio('Onderdelen',
                 ["Introductie", "Aannames", "Informatie terrein","Energiebehoefte","Conclusie/Aanbevelingen"])

# ======================================================================================================================================================================
if blog_post == 'Introductie':
  st.header('Inleiding')
# ======================================================================================================================================================================
elif blog_post == 'Aannames':
  st.header('Aannames')
  st.write("""
    **Aannames voor de dataset van de hackathon:**

  1. **Bedrijven in de fruit-, groente- of aardappelsector:**
   - Bij lokale leveringen rijdt een vrachtwagen gemiddeld 200 km per dag.
   - Bij nationale leveringen rijdt een vrachtwagen gemiddeld 450 km per dag.
   - Bij internationale leveringen rijdt een vrachtwagen gemiddeld 800 km per dag.

  2. **Bedrijven in de logistieke sector:**
   - Bij lokale leveringen rijdt een vrachtwagen gemiddeld 200 km per dag.
   - Bij nationale leveringen rijdt een vrachtwagen gemiddeld 450 km per dag.
   - Bij internationale leveringen rijdt een vrachtwagen gemiddeld 800 km per dag.
   - Voor langeafstandstrajecten rijdt een vrachtwagen meer dan 1.000 km per dag, tot ongeveer 1.500 km.

  **Basis voor geschatte gereden kilometers van bestelwagens, personenauto's en elektrische voertuigen:**
  - De schattingen zijn per sector verdeeld:
  - Voor bedrijven die frequent aan klanten leveren, zijn hogere schattingen gemaakt voor de kilometers gereden met bestelwagens.
  - Voor bedrijven die investeren in duurzaamheid zijn de geschatte kilometers voor elektrische voertuigen lager dan die voor bestelwagens.
  - De geschatte kilometers voor personenauto's zijn lager, aangezien deze minder vaak zakelijk worden ingezet dan vrachtwagens of bestelauto's.

  **Basis voor ritpatronen:**
  - **Ritpatronen:** De gekozen tijdstippen zijn gebaseerd op de logistieke en voedingssector, waar vroege leveringen gebruikelijk zijn om verse producten bij klanten te garanderen.
  - **Sectoroverwegingen:** Voor bedrijven in de verse-/koeltransportsector zijn vroege ochtendleveringen gebruikelijk. Andere sectoren met bredere distributiepatronen kunnen later op de dag leveren.

  **Aantal ritten per dag:**
  - De schattingen zijn gebaseerd op de behoeften van bedrijven in de groente- en fruitsector, evenals in de logistieke en koeltransportsector.

  **Basis voor energieverbruik zonder gereden kilometers:**
  - **Bestelwagens:** Het energieverbruik is geschat op basis van het gemiddelde verbruik in de sector.
  - **Elektrische voertuigen:** Het verbruik is afhankelijk van het type voertuig en het gebruik binnen de sector.
  - **Personenauto's:** Het verbruik is geschat op basis van het gemiddelde verbruik per auto.
  - **Vrachtwagens:** Specifiek voor koeltrucks in de koel-/logistieke sector, waarbij continu koeling vereist is, waardoor het energieverbruik hoger ligt.

  **Energieverbruik per kilometer:**
  - **Vrachtwagens:** Internationale vrachtwagens verbruiken ongeveer 35 liter brandstof per 100 km (3,5 liter per km). Aangezien één liter diesel 10 kWh bevat, komt dit neer op 35 kWh/km.
  - **Bestelwagens:** Bestelwagens verbruiken ongeveer 11 liter diesel per 100 km (1,1 liter per km), wat gelijkstaat aan 11 kWh/km.
  - **Elektrische voertuigen:** Deze rijden ongeveer 5 km op 1 kWh, wat neerkomt op 0,2 kWh/km.
  - **Personenauto's:**
    - Benzineauto's rijden ongeveer 15 km op 1 liter benzine. Eén liter benzine bevat circa 8,9 kWh, wat resulteert in 0,59 kWh/km. Het aandeel benzineauto's in Nederland is 76,11% (CBS).
    - Dieselauto's rijden ongeveer 21 km op 1 liter diesel, met een energiewaarde van 10 kWh per liter, wat neerkomt op 0,48 kWh/km. Het aandeel dieselauto's in Nederland is 8,2% (CBS).

  **Schatting laadtijden:**
  - Laadtijden zijn afhankelijk van de lading, het type voertuig en de sector waarin het bedrijf actief is.

  **Schatting van het aantal voertuigen:**
  - **Vrachtwagens:** Geschat op basis van de behoefte aan transport van grote ladingen, vooral in de voedings- en koeltransportsector.
  - **Bestelwagens:** Geschat voor kleinere leveringen en distributie naar klanten en winkels.
  - **Elektrische voertuigen:** Aangenomen op basis van de trend naar duurzaamheid en de toename van elektrisch vervoer in de sector.
  - **Personenauto's:** Geschat voor personeel en kleine zakelijke ritten.

  **Elektrificatiegraad:**
  - De elektrificatiegraad groeit lineair tot het jaar 2050.

  **Bronnen:**
  - Transport en Logistiek Nederland (TLN): [tln.nl](https://www.tln.nl)
  - Rijksdienst voor Ondernemend Nederland (RVO): [rvo.nl](https://www.rvo.nl)
  - Sectorrapporten van Panteia en CBS: [cbs.nl](https://www.cbs.nl) en [panteia.nl](https://www.panteia.nl)
  """)

#======================================================================================================================================================================
elif blog_post == 'Informatie terrein':
    dfp_data = pd.read_csv("Data/DutchFreshPort.csv",sep=";")
    APN_data = pd.read_csv("Data/AmsterdamPoortNoord.csv",sep=",")

    dfp_data.dropna(axis=0, how='all', inplace=True)
    dfp_data = dfp_data.drop(dfp_data.index[-1])
  
    st.header('Imformatie Terreinen')
    st.write("""
    Op dit dashboard krijg je inzicht in twee belangrijke bedrijventerreinen in Nederland: Dutch Fresh Port en Amsterdam Poort Noord. Beide locaties spelen een 
    cruciale rol in de logistiek en handel, maar hebben elk hun eigen unieke kenmerken en sectoren.
    
    Dutch Fresh Port, gelegen in de regio Ridderkerk en Barendrecht, staat bekend als een belangrijk knooppunt voor de agro- en verslogistiek. Het bedrijventerrein 
    herbergt tal van bedrijven die zich richten op de productie, verwerking, en distributie van verse producten, zoals groenten, fruit en bloemen. Dankzij de 
    nabijheid van logistieke hubs en goede verbindingen met de Rotterdamse haven en het wegennet, is het een strategische locatie voor bedrijven in de voedselketen.
    
    Aan de andere kant ligt Amsterdam Poort Noord, een bedrijventerrein in het noorden van Amsterdam. Dit terrein richt zich voornamelijk op een mix van commerciële 
    en industriële bedrijven, met een focus op distributie, productie en handel. De nabijheid van het centrum van Amsterdam en de grote internationale luchthaven 
    Schiphol maakt het een aantrekkelijke locatie voor bedrijven die snelle toegang tot zowel de stad als internationale markten nodig hebben.
    
    Waar Dutch Fresh Port sterk gericht is op versproducten en logistiek, biedt Amsterdam Poort Noord een breder scala aan sectoren. Het verschil in locatie zorgt 
    ervoor dat beide terreinen verschillende logistieke voordelen hebben: Dutch Fresh Port profiteert van de nabijheid van de Rotterdamse haven, terwijl Amsterdam 
    Poort Noord dicht bij de hoofdstad en Schiphol ligt.""")
    
    bedrijventerrein = st.selectbox("Kies een model:", ["Dutch Fresh Port", "Amsterdam Poort Noord"])
    
    if bedrijventerrein == 'Dutch Fresh Port':

        # Functie om markers toe te voegen
        def marker_toevoegen(adres, popup_adres, popup_sector, tooltip):
            geolocator = Nominatim(user_agent="mijn_applicatie")
            try:
                locatie = geolocator.geocode(adres)
                if locatie:
                    # HTML layout voor de popup
                    html = f"""
                    <div style="width:300px;">
                    <table style="width:100%;">
                    <tr><th>Adres:</th><td>{popup_adres}</td></tr>
                    <tr><th>Sector:</th><td>{popup_sector}</td></tr>
                    </table>
                    </div>
                    """
                    popup = folium.Popup(html, max_width=300)
                
                    # Marker toevoegen met aangepaste popup
                    folium.Marker(location=[locatie.latitude, locatie.longitude],
                                  popup=popup,
                                  tooltip=tooltip).add_to(m)
                else:
                    print(f"Adres niet gevonden: {adres}")
            except Exception as e:
                print(f"Fout bij geocoderen van {adres}: {e}")
        # Maak de map
        m = folium.Map(location=[51.8609276, 4.56141703], zoom_start=14,map = "OpenStreetMap")
        
        # Polyline toevoegen
        coordinates = [
            [51.86467654, 4.544055401],
            [51.870874572133, 4.5701179918743], 
            [51.86086497557, 4.5899717563522],
            [51.85067, 4.55772],
            [51.86467654, 4.544055401]
        ]
        folium.PolyLine(locations=coordinates, color='blue', weight=5, opacity=0.7).add_to(m)

        # Voeg markers toe op basis van gegevens in dfp_data
        for index, row in dfp_data.iterrows():
            marker_toevoegen(row['Adres'], row["Adres"], row["Sector"], row["Bedrijfsnaam"])
        # Toon de map
        st_folium(m, width=700, height=500)

    else :
      bedrijventerrein == 'Amsterdam Poort Noord':
    #     # Functie om markers toe te voegen
    #     def marker_toevoegen(adres, popup_adres, popup_sector, tooltip):
    #         geolocator = Nominatim(user_agent="mijn_applicatie")
    #         try:
    #             locatie = geolocator.geocode(adres)
    #             if locatie:
    #                 # HTML layout voor de popup
    #                 html = f"""
    #                 <div style="width:300px;">
    #                 <table style="width:100%;">
    #                 <tr><th>Adres:</th><td>{popup_adres}</td></tr>
    #                 <tr><th>Sector:</th><td>{popup_sector}</td></tr>
    #                 </table>
    #                 </div>
    #                 """
    #                 popup = folium.Popup(html, max_width=300)
                    
    #                 # Marker toevoegen met popup
    #                 folium.Marker(location=[locatie.latitude, locatie.longitude],
    #                               popup=popup,
    #                               tooltip=tooltip).add_to(m)
    #         except: "done"

          def marker_toevoegen(adres, popup_adres, popup_sector, tooltip):
              geolocator = Nominatim(user_agent="mijn_applicatie")
              try:
                  locatie = geolocator.geocode(adres)
                  if locatie:
                      # HTML layout voor de popup
                      html = f"""
                      <div style="width:300px;">
                      <table style="width:100%;">
                      <tr><th>Adres:</th><td>{popup_adres}</td></tr>
                      <tr><th>Sector:</th><td>{popup_sector}</td></tr>
                      </table>
                      </div>
                      """
                      popup = folium.Popup(html, max_width=300)
                
                      # Marker toevoegen met aangepaste popup
                      folium.Marker(location=[locatie.latitude, locatie.longitude],
                                    popup=popup,
                                    tooltip=tooltip).add_to(m)
                  else:
                      print(f"Adres niet gevonden: {adres}")
              except Exception as e:
                  print(f"Fout bij geocoderen van {adres}: {e}")

# Maak de map
m = folium.Map(location=[52.395724, 4.789207], zoom_start=15, map = "OpenStreetMap")
# Polyline toevoegen
coordinates = [
    [52.397554, 4.774426],
    [52.393480, 4.772532], 
    [52.393480, 4.806433],
    [52.397554, 4.802787],
    [52.397554, 4.774426]
]
folium.PolyLine(locations=coordinates, color='blue', weight=5, opacity=0.7).add_to(m)
# Voeg markers toe op basis van gegevens in APN_data
dfp_data = pd.read_csv("Data/DutchFreshPort.csv",sep=";")
APN_data = pd.read_csv("Data/AmsterdamPoortNoord.csv",sep=",")

dfp_data.dropna(axis=0, how='all', inplace=True)
dfp_data = dfp_data.drop(dfp_data.index[-1])
for index, row in APN_data.iterrows():
    marker_toevoegen(row['Adres'], row["Adres"], row["Sector"], row["Bedrijfsnaam"])

# Toon de map
st_folium(m, width=700, height=500)
  

# ======================================================================================================================================================================
if blog_post == 'Energiebehoefte':
  st.header("Energiebehoefte", divider='gray')
  st.write("De hoeveelheid kilowattuur (kWh) blijft het belangrijkste om te bepalen als het gaat om het verduurzamen van de mobiliteit van een bedrijventerrein. Deze statistiek laat zien hoeveel kWh elk bedrijf nodig heeft om alles elektrisch te kunnen maken. Door eerst baseline te bepalen, kan er vanuit daar een voorspelling gedaan worden over hoeveelheid kWh die nodig is om in 2050 helemaal elektrisch te zijn. Deze voorspelling komt voort uit de data en de eerder genoemde aannames.")
  st.write("Kies hieronder een sector en selecteer daarna in de legenda welk bedrijf u wilt analyseren. De grafiek zal alle bedrijven, van het bedrijventerrein Dutch Fresh Port, tonen die werkzaam zijn in die sector met de voorspelling hoeveel kWh er nodig is voor elke dag in 2025.") 
  
  dfp = pd.read_csv('Data/DutchFreshPort.csv', sep=";")
  dfp['Aantal parkeerplekken'] = dfp['Aantal parkeerplekken'].fillna(dfp.groupby('Sector')['Aantal parkeerplekken'].transform('median'))
  dfp['Aantal bezette parkeerplekken '] = dfp['Aantal bezette parkeerplekken '].fillna(dfp.groupby('Sector')['Aantal bezette parkeerplekken '].transform('median'))
  dfp['Aantal laad/losplekken'] = dfp['Aantal laad/losplekken'].fillna(dfp.groupby('Sector')['Aantal laad/losplekken'].transform('median'))
  dfp['Aantal bezette laad/losplekken'] = dfp['Aantal bezette laad/losplekken'].fillna(dfp.groupby('Sector')['Aantal bezette laad/losplekken'].transform('median'))
  dfp.rename(columns={'Energieverbruik bestelbussen (kWh)':'Energieverbruik bestelbussen zonder km (kWh)',
                      'Energieverbruik elektrische voertuigen (kWh)':'Energieverbruik elektrische voertuigen zonder km (kWh)',
                      "Energieverbruik personenauto's (kWh)":"Energieverbruik personenauto's zonder km (kWh)",
                      'Energieverbruik trucks (kWh)':'Energieverbruik trucks zonder km'}, inplace = True)
  
  # Baseline bepalen
  energieverbruik_trucks = 35
  energieverbruik_bestelbus = 11
  energieverbruik_elektrische_voertuigen = 0.2
  energieverbruik_benzine_personenauto = 0.59
  energieverbruik_diesel_personenauto = 0.48
  
  kolommen_om_te_zetten = [
      "Aantal Trucks",
      "Aantal gereden kilometers trucks per dag",
      "Aantal bestelauto's",
      "Aantal gereden kilometers bestelbussen per dag",
      "Aantal elektrische voertuigen",
      "Aantal gereden kilometers elektrische voertuigen per dag",
      "Aantal personenauto's",
      "Aantal gereden kilometers personenauto's per dag",
      "Energieverbruik trucks zonder km",
      'Aantal ritten per dag trucks', 
      'Aantal ritten per dag bestelbussen',
      'Aantal ritten per dag elektrische voertuigen',
      "Aantal ritten per dag personenauto's",
      "Energieverbruik bestelbussen zonder km (kWh)",
      "Energieverbruik elektrische voertuigen zonder km (kWh)",
      "Energieverbruik personenauto's zonder km (kWh)"
  ]
  
  for kolom in kolommen_om_te_zetten:
      dfp[kolom] = pd.to_numeric(dfp[kolom], errors='coerce')
  
  def bereken_totaal_energieverbruik_trucks(row):
      return row['Energieverbruik trucks zonder km'] + (row['Aantal ritten per dag trucks'] * row['Aantal gereden kilometers trucks per dag'] * energieverbruik_trucks)
  
  def bereken_totaal_energieverbruik_bestelbus(row):
      return row['Energieverbruik bestelbussen zonder km (kWh)'] + (row["Aantal ritten per dag bestelbussen"] * row["Aantal gereden kilometers bestelbussen per dag"] * energieverbruik_bestelbus)
  
  def bereken_totaal_energieverbruik_elektrische_voertuigen(row):
      return row['Energieverbruik elektrische voertuigen zonder km (kWh)'] + (row['Aantal ritten per dag elektrische voertuigen'] * row['Aantal gereden kilometers elektrische voertuigen per dag'] * energieverbruik_elektrische_voertuigen)
  
  def bereken_totaal_energieverbruik_personenauto(row):
      perc_benzine = 0.7611
      perc_diesel = 0.0822
      return (row["Energieverbruik personenauto's zonder km (kWh)"] + (row["Aantal ritten per dag personenauto's"] * row["Aantal gereden kilometers personenauto's per dag"] * energieverbruik_benzine_personenauto) * perc_benzine) + (row["Energieverbruik personenauto's zonder km (kWh)"] + (row["Aantal ritten per dag personenauto's"] * row["Aantal gereden kilometers personenauto's per dag"] * energieverbruik_diesel_personenauto) * perc_diesel)
  
  def bereken_totaal_energieverbruik(row):
      return (row['Totale energieverbruik trucks kWh'] + 
              row["Totale energieverbruik bestelbussen kWh"] + 
              row['Totale energieverbruik elektrische voertuigen kWh'] + 
              row["Totale energieverbruik personenauto's"])
  
  dfp['Totale energieverbruik bestelbussen kWh'] = dfp.apply(bereken_totaal_energieverbruik_bestelbus, axis=1)
  dfp['Totale energieverbruik elektrische voertuigen kWh'] = dfp.apply(bereken_totaal_energieverbruik_elektrische_voertuigen, axis=1)  
  dfp["Totale energieverbruik personenauto's"] = dfp.apply(bereken_totaal_energieverbruik_personenauto, axis=1)
  dfp['Totale energieverbruik trucks kWh'] = dfp.apply(bereken_totaal_energieverbruik_trucks, axis=1)
  dfp['Totale energieverbruik voertuigen kWh'] = dfp.apply(bereken_totaal_energieverbruik, axis=1)
  
  # Toekomst bepalen
  # Huidige elektrificatiegraad: 2.3% in 2024 (Dutch Fresh Port)
  huidige_elektrificatiegraad = 0.023
  # Doelstelling: 100% in 2050
  doelstelling = 1
  # Aantal jaren: 26
  aantal_jaren = 26
  # Jaarlijkse elektrificatiegraad: 3.76%
  jaarlijkse_groei = (doelstelling - huidige_elektrificatiegraad)/aantal_jaren
  dagelijkse_groei = (doelstelling - huidige_elektrificatiegraad)/(aantal_jaren * 365)
  uurlijkse_groei = (doelstelling - huidige_elektrificatiegraad)/(aantal_jaren * 365*24)
  
  def bereken_toekomstige_energiebehoefte(row):
      return row['Totale energieverbruik voertuigen kWh'] * (1 + jaarlijkse_groei)
  
  def bereken_verschil_energiebehoefte(row):
      return row['Toekomstige energiebehoefte kWh per dag'] - row['Totale energieverbruik voertuigen kWh']
  
  def bereken_huidig_energiebehoefte_uur(row):
      return row['Totale energieverbruik voertuigen kWh']/24
  
  def bereken_toekomstige_energiebehoefte_uur(row):
      return row['Toekomstige energiebehoefte kWh per dag']/24
  
  dfp['Toekomstige energiebehoefte kWh per dag'] = dfp.apply(bereken_toekomstige_energiebehoefte, axis=1)
  dfp['Verschil energiebehoefte 1 jaar (3,76%)'] = dfp.apply(bereken_verschil_energiebehoefte, axis=1)
  dfp['Totale energieverbruik voertuigen kWh per uur'] = dfp.apply(bereken_huidig_energiebehoefte_uur, axis=1)
  dfp['Toekomstige energiebehoefte kWh per uur'] = dfp.apply(bereken_toekomstige_energiebehoefte_uur, axis=1)
  
  test_date = datetime.datetime.strptime("01-01-2025", "%d-%m-%Y")
  date_generated = pd.date_range(test_date, periods = 365, freq="D")
  
  uren = pd.date_range("00:00", "23:00", freq="h").time
  
  multi_index = pd.MultiIndex.from_product([date_generated, uren], 
                                           names=["Datum", "Uren"])
  df= pd.DataFrame(index=multi_index, columns =['4 Fruit Company', 'A.F.L. Barendrecht', 'Agrofair Benelux',
                                                'Allround Cargo Handling', 'Ambtman jr. Import Export B.V.', 'Bakker Barendrecht', 'Berkman Groep',
                                                'Best trucks', 'Blankendaal Cold Stores B.V.', 'Broom Frio Holding', 'CMR Holland B.V.',
                                                'Consistence', 'Davis Global B.V.', 'Davis Pure Foods B.V.', 'Dijco', 'Europe Retail Packing',
                                                'Fortuna Frutos', 'Four Seasons Fruit Supply B.V.', 'Fresh Pack Logistics', 'Fresh Pride',
                                                'Fresh2You', 'Frigoscandia B.V.', 'Frosinn B.V.', 'FruitOne Europe B.V.',
                                                'Frukar B.V.', 'Frutyco B.V.', 'Hars & Hagebauer B.V.', 'Hoofdman & Roodzand B.V.',
                                                'Jaguar the Fresh Company B.V.', 'JP Fruit Packing Service', 'Keelings Fresh International Limited',
                                                'KivitsGoes Handling', 'Koninklijke Euser', 'Koring', 'Lazy Foods', 'LCL Logistics',
                                                'Looije Packing', 'Meeder Group', 'Niva Fresh International', 'OV Fruit B.V.', 'Purnatur',
                                                'R&M Forwarding', 'ReFruit B.V.', 'Rivafruit B.V.', 'Rungis B.V.', 'Sawari Fresh International B.V.',
                                                'The Greenery', 'Torres Tropical B.V.', 'Van Gelder Groente & Fruit', 'Van Ooijen Citrus B.V.',
                                                'Van Vugt Kruiden', 'VDH Forwarding & Warehousing B.V.', 'VerDi Import B.V.', 'Verita Holland B.V.',
                                                'Very Fruity B.V.', 'VGK Cool Logistics B.V.', 'Zoutewelle Import Export B.V.']
  )
  # Invullen van de dataframe
  dfp_clean = dfp[['Bedrijfsnaam', 'Rittenpatronen', 'Laadpatronen', 'Totale energieverbruik voertuigen kWh', 'Toekomstige energiebehoefte kWh per dag', 
                   'Totale energieverbruik voertuigen kWh per uur', 'Toekomstige energiebehoefte kWh per uur']]
  df.loc[:, '4 Fruit Company'] = dfp_clean.loc[0, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'A.F.L. Barendrecht'] = dfp_clean.loc[1, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Agrofair Benelux'] = dfp_clean.loc[2, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Allround Cargo Handling'] = dfp_clean.loc[3, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Ambtman jr. Import Export B.V.'] = dfp_clean.loc[4, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Bakker Barendrecht'] = dfp_clean.loc[5, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Berkman Groep'] = dfp_clean.loc[6, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Best trucks'] = dfp_clean.loc[7, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Blankendaal Cold Stores B.V.'] = dfp_clean.loc[8, 'Toekomstige energiebehoefte kWh per uur']
  
  df.loc[:, 'Broom Frio Holding'] = dfp_clean.loc[9, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'CMR Holland B.V.'] = dfp_clean.loc[10, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Consistence'] = dfp_clean.loc[11, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Davis Global B.V.'] = dfp_clean.loc[12, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Davis Pure Foods B.V.'] = dfp_clean.loc[13, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Dijco'] = dfp_clean.loc[14, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Europe Retail Packing'] = dfp_clean.loc[15, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Fortuna Frutos'] = dfp_clean.loc[16, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Four Seasons Fruit Supply B.V.'] = dfp_clean.loc[17, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Fresh Pack Logistics'] = dfp_clean.loc[18, 'Toekomstige energiebehoefte kWh per uur']
  
  df.loc[:, 'Fresh Pride'] = dfp_clean.loc[19, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Fresh2You'] = dfp_clean.loc[20, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Frigoscandia B.V.'] = dfp_clean.loc[21, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Frosinn B.V.'] = dfp_clean.loc[22, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'FruitOne Europe B.V.'] = dfp_clean.loc[23, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Frukar B.V.'] = dfp_clean.loc[24, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Frutyco B.V.'] = dfp_clean.loc[25, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Hars & Hagebauer B.V.'] = dfp_clean.loc[26, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Hoofdman & Roodzand B.V.'] = dfp_clean.loc[27, 'Toekomstige energiebehoefte kWh per uur']
  
  df.loc[:, 'Jaguar the Fresh Company B.V.'] = dfp_clean.loc[28, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'JP Fruit Packing Service'] = dfp_clean.loc[29, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Keelings Fresh International Limited'] = dfp_clean.loc[30, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'KivitsGoes Handling'] = dfp_clean.loc[31, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Koninklijke Euser'] = dfp_clean.loc[32, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Koring'] = dfp_clean.loc[33, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Lazy Foods'] = dfp_clean.loc[34, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'LCL Logistics'] = dfp_clean.loc[35, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Looije Packing'] = dfp_clean.loc[36, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Meeder Group'] = dfp_clean.loc[37, 'Toekomstige energiebehoefte kWh per uur']
  
  df.loc[:, 'Niva Fresh International'] = dfp_clean.loc[38, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'OV Fruit B.V.'] = dfp_clean.loc[39, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Purnatur'] = dfp_clean.loc[40, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'R&M Forwarding'] = dfp_clean.loc[41, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'ReFruit B.V.'] = dfp_clean.loc[42, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Rivafruit B.V.'] = dfp_clean.loc[43, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Rungis B.V.'] = dfp_clean.loc[44, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Sawari Fresh International B.V.'] = dfp_clean.loc[45, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'The Greenery'] = dfp_clean.loc[46, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Torres Tropical B.V.'] = dfp_clean.loc[47, 'Toekomstige energiebehoefte kWh per uur']
  
  df.loc[:, 'Van Gelder Groente & Fruit'] = dfp_clean.loc[48, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Van Ooijen Citrus B.V.'] = dfp_clean.loc[49, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Van Vugt Kruiden'] = dfp_clean.loc[50, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'VDH Forwarding & Warehousing B.V.'] = dfp_clean.loc[51, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'VerDi Import B.V.'] = dfp_clean.loc[52, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Verita Holland B.V.'] = dfp_clean.loc[53, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Very Fruity B.V.'] = dfp_clean.loc[54, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'VGK Cool Logistics B.V.'] = dfp_clean.loc[55, 'Toekomstige energiebehoefte kWh per uur']
  df.loc[:, 'Zoutewelle Import Export B.V.'] = dfp_clean.loc[56, 'Toekomstige energiebehoefte kWh per uur']
  
  for index, row in dfp_clean.iterrows():
      bedrijf = row['Bedrijfsnaam']
      energiebehoefte = row['Toekomstige energiebehoefte kWh per uur']
      df.loc[(test_date, slice(None)), bedrijf] = energiebehoefte 
  
  groei_per_dag = (1 + dagelijkse_groei)
  
  factoren_per_dag = [groei_per_dag ** i for i in range(len(date_generated))]
  
  factoren_voor_uren = pd.Series(factoren_per_dag).repeat(24).values
  
  for bedrijf in df.columns:
      df.loc[:, bedrijf] = round(df.loc[:, bedrijf].fillna(0) * factoren_voor_uren,)
  
  df_handel_sector = df[['4 Fruit Company', 'Ambtman jr. Import Export B.V.', 'Bakker Barendrecht', 'Broom Frio Holding', 'CMR Holland B.V.',
                         'Davis Global B.V.', 'Europe Retail Packing', 'Fortuna Frutos', 'Fresh Pride', 'Fresh2You', 
                         'Frosinn B.V.', 'FruitOne Europe B.V.', 'Frukar B.V.', 'Frutyco B.V.', 'Hars & Hagebauer B.V.',
                         'Hoofdman & Roodzand B.V.', 'Jaguar the Fresh Company B.V.', 'Keelings Fresh International Limited',
                         'Niva Fresh International', 'OV Fruit B.V.', 'OV Fruit B.V.', 'Purnatur', 'Rivafruit B.V.',
                         'Rungis B.V.', 'Sawari Fresh International B.V.', 'Torres Tropical B.V.', 'Van Gelder Groente & Fruit',
                         'Van Ooijen Citrus B.V.', 'Van Vugt Kruiden', 'VerDi Import B.V.', 'Verita Holland B.V.', 'Zoutewelle Import Export B.V.']]
  
  df_logistiek_sector = df[['A.F.L. Barendrecht', 'Allround Cargo Handling', 'Bakker Barendrecht', 'Blankendaal Cold Stores B.V.',
                            'Broom Frio Holding', 'CMR Holland B.V.', 'Davis Global B.V.', 'Davis Pure Foods B.V.', 'Europe Retail Packing',
                            'Fortuna Frutos', 'Four Seasons Fruit Supply B.V.', 'Fresh Pack Logistics', 'Frigoscandia B.V.',
                            'Frosinn B.V.', 'FruitOne Europe B.V.', 'Hoofdman & Roodzand B.V.', 'JP Fruit Packing Service',
                            'KivitsGoes Handling', 'Koninklijke Euser', 'Koring', 'LCL Logistics', 'Looije Packing', 'Meeder Group',
                            'R&M Forwarding', 'The Greenery', 'Van Gelder Groente & Fruit', 'VDH Forwarding & Warehousing B.V.',
                            'VerDi Import B.V.', 'VGK Cool Logistics B.V.']]
  
  df_transport_sector = df[['A.F.L. Barendrecht', 'Four Seasons Fruit Supply B.V.', 'Fresh Pack Logistics',
                            'Frigoscandia B.V.', 'Frosinn B.V.', 'LCL Logistics', 'VGK Cool Logistics B.V.']]
  
  df_overig_sector = df[['Agrofair Benelux', 'Berkman Groep', 'Best trucks', 'Consistence', 'Dijco', 
                         'KivitsGoes Handling', 'Lazy Foods', 'ReFruit B.V.', 'Very Fruity B.V.']]
  
  sectoren = ['Handelsector', 'Logistieksector', 'Transportsector', 'Overige sector']
  sectoren_dict = {
      'Handelsector': df_handel_sector,
      'Logistieksector': df_logistiek_sector,
      'Transportsector': df_transport_sector,
      'Overige sector': df_overig_sector
  }
  
  df_daily_handel_sector = df_handel_sector.groupby('Datum').sum()
  df_daily_logistiek_sector = df_logistiek_sector.groupby('Datum').sum()
  df_daily_transport_sector = df_logistiek_sector.groupby('Datum').sum()
  df_daily_overig_sector = df_overig_sector.groupby('Datum').sum()
  
  sector_selectie = st.selectbox('Selecteer een sector', sectoren)
  geselecteerd_df = sectoren_dict[sector_selectie]
  
  if sector_selectie == 'Handelsector':
  
      fig_handel_sector = go.Figure()
  
      for bedrijf in df_daily_handel_sector.columns:
          fig_handel_sector.add_trace(go.Scatter(
              x=df_daily_handel_sector.index,
              y=df_daily_handel_sector[bedrijf],
              mode='lines+markers',
              name=bedrijf
          ))
      
      fig_handel_sector.update_layout(
          title='Toekomstige energiebehoefte voor Handelsector (2025) in kWh per dag',
          xaxis_title='Datum',
          yaxis_title='Energiebehoefte in kWh',
          legend_title='Bedrijf',
          template='plotly_white'
      )
  
      st.plotly_chart(fig_handel_sector)
  
  elif sector_selectie == 'Logistieksector':
  
      fig_logistiek_sector = go.Figure()
  
      for bedrijf in df_daily_logistiek_sector.columns:
          fig_logistiek_sector.add_trace(go.Scatter(
              x=df_daily_logistiek_sector.index,
              y=df_daily_logistiek_sector[bedrijf],
              mode='lines+markers',
              name=bedrijf
          ))
      
      fig_logistiek_sector.update_layout(
          title='Toekomstige energiebehoefte voor bedrijven in de Logistieksector (2025) in kWh per dag',
          xaxis_title='Datum',
          yaxis_title='Energiebehoefte in kWh',
          legend_title='Bedrijf',
          template='plotly_white'
      )
  
      st.plotly_chart(fig_logistiek_sector)
  
  elif sector_selectie == 'Transportsector':
  
      fig_transport_sector = go.Figure()
  
      for bedrijf in df_daily_transport_sector.columns:
          fig_transport_sector.add_trace(go.Scatter(
              x=df_daily_transport_sector.index,
              y=df_daily_transport_sector[bedrijf],
              mode='lines+markers',
              name=bedrijf
          ))
      
      fig_transport_sector.update_layout(
          title='Toekomstige energiebehoefte voor bedrijven in de Transportsector (2025) in kWh per dag',
          xaxis_title='Datum',
          yaxis_title='Energiebehoefte in kWh',
          legend_title='Bedrijf',
          template='plotly_white'
      )
  
      st.plotly_chart(fig_transport_sector)
  
  elif sector_selectie == 'Overige sector':
  
      fig_overig_sector = go.Figure()
  
      for bedrijf in df_daily_overig_sector.columns:
          fig_overig_sector.add_trace(go.Scatter(
              x=df_daily_overig_sector.index,
              y=df_daily_overig_sector[bedrijf],
              mode='lines+markers',
              name=bedrijf
          ))
      
      fig_overig_sector.update_layout(
          title='Toekomstige energiebehoefte voor bedrijven in de overige sectoren (2025) in kWh per dag',
          xaxis_title='Datum',
          yaxis_title='Energiebehoefte in kWh',
          legend_title='Bedrijf',
          template='plotly_white'
      )
  
      st.plotly_chart(fig_overig_sector)
# ======================================================================================================================================================================
elif blog_post == 'Conclusie/Aanbevelingen':
  st.header('Conclusie/Aanbevelingen')
  st.write("""
**De toekomstige energiebehoefte van mobiliteit op bedrijventerreinen zal in 2025 aanzienlijk toenemen, voornamelijk door de groeiende vraag naar transport en logistieke diensten in de vers- en levensmiddelenindustrie. Om aan deze stijgende vraag te voldoen, is een strategische aanpak nodig die gericht is op duurzame groei en een efficiënte energietransitie.**

Een belangrijk doel is dat tegen 2050 alle voertuigen die worden gebruikt voor transport, zoals vrachtwagens, volledig elektrisch zijn. Deze transitie naar elektrisch vervoer is essentieel om de CO2-uitstoot te verminderen en te voldoen aan de klimaatdoelstellingen. Bovendien biedt het overstappen op elektrische voertuigen aanzienlijke voordelen op het gebied van luchtkwaliteit en geluidsoverlast, wat bijdraagt aan een schonere en gezondere leefomgeving op en rond deze bedrijventerreinen.

**De verandering naar elektrische mobiliteit brengt echter ook verschillende uitdagingen met zich mee, met name op het gebied van logistiek en infrastructuur.** Het vereist een aanzienlijke uitbreiding van de laadinfrastructuur, met voldoende laadpunten voor vrachtwagens en andere elektrische voertuigen. Daarbij is het van cruciaal belang om een stabiele energievoorziening te waarborgen en slim energiemanagement toe te passen. Dit helpt niet alleen om piekbelastingen op te vangen, maar ook om energie efficiënt te gebruiken.

**Om de benodigde veranderingen te realiseren, zijn verschillende strategieën en samenwerkingsverbanden van essentieel belang.** Dit omvat onder andere investeringen in innovatieve technologieën, zoals slimme laadoplossingen en duurzame energiebronnen, zoals zonne-energie en windenergie. Samenwerking met relevante stakeholders in de logistieke keten is ook van groot belang, van leveranciers tot lokale overheden, om een gezamenlijke visie te ontwikkelen en synergieën te creëren.

**Hoewel de logistieke opgave groot is, is deze niet onhaalbaar.** Door tijdig te investeren in infrastructuur, innovatieve technologieën toe te passen en intensief samen te werken met partners in de keten, kunnen we deze overgang succesvol maken. Het is cruciaal om de komende jaren gericht te werken aan een stapsgewijze vergroening van de mobiliteit. Dit stelt ons in staat om in 2050 een volledig elektrisch en duurzaam transportsysteem te realiseren, dat niet alleen voldoet aan de energievraag, maar ook bijdraagt aan een leefbare en duurzame toekomst voor iedereen.
""")

