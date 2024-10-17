import streamlit as st

# from steamlit_gallery import apps, componetns
# from streamlit_gallery import page_group

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
if blog_post == 'Informatie terrein':
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
            except: "done"

        # Maak de map
        m = folium.Map(location=[51.8609276, 4.56141703], zoom_start=14)
        
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
        m

  

# ======================================================================================================================================================================
#elif blog_post == 'Energiebehoefte':
# ======================================================================================================================================================================
#elif blog_post == 'Conclusie/Aanbevelingen':
