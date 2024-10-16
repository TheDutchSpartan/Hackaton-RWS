import streamlit as st

# from steamlit_gallery import apps, componetns
# from streamlit_gallery import page_group

blog_post=st.sidebar.radio('Onderdelen',
                 ["Introductie", "Aannames", "Informatie terrein","Energiebehoefte","Conclusie/Aanbevelingen"])

# ======================================================================================================================================================================
if blog_post == 'Introductie':
  st.header('Inleiding')
# ======================================================================================================================================================================
elif blog_post == ' Aannames':
  st.header('Aanames')
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

  **Basis voor geschatte gereden kilometers van bestelwagens, personenauto`s en elektrische voertuigen:**
  - De schattingen zijn per sector verdeeld:
  - Voor bedrijven die frequent aan klanten leveren, zijn hogere schattingen gemaakt voor de kilometers gereden met bestelwagens.
  - Voor bedrijven die investeren in duurzaamheid zijn de geschatte kilometers voor elektrische voertuigen lager dan die voor bestelwagens.
  - De geschatte kilometers voor personenauto`s zijn lager, aangezien deze minder vaak zakelijk worden ingezet dan vrachtwagens of bestelauto`s.

  **Basis voor ritpatronen:**
  - **Ritpatronen:** De gekozen tijdstippen zijn gebaseerd op de logistieke en voedingssector, waar vroege leveringen gebruikelijk zijn om verse producten bij klanten te garanderen.
  - **Sectoroverwegingen:** Voor bedrijven in de verse-/koeltransportsector zijn vroege ochtendleveringen gebruikelijk. Andere sectoren met bredere distributiepatronen kunnen later op de dag leveren.

  **Aantal ritten per dag:**
  - De schattingen zijn gebaseerd op de behoeften van bedrijven in de groente- en fruitsector, evenals in de logistieke en koeltransportsector.

  **Basis voor energieverbruik zonder gereden kilometers:**
  - **Bestelwagens:** Het energieverbruik is geschat op basis van het gemiddelde verbruik in de sector.
  - **Elektrische voertuigen:** Het verbruik is afhankelijk van het type voertuig en het gebruik binnen de sector.
  - **Personenauto`s:** Het verbruik is geschat op basis van het gemiddelde verbruik per auto.
  - **Vrachtwagens:** Specifiek voor koeltrucks in de koel-/logistieke sector, waarbij continu koeling vereist is, waardoor het energieverbruik hoger ligt.

  **Energieverbruik per kilometer:**
  - **Vrachtwagens:** Internationale vrachtwagens verbruiken ongeveer 35 liter brandstof per 100 km (3,5 liter per km). Aangezien één liter diesel 10 kWh bevat, komt dit neer op 35 kWh/km.
  - **Bestelwagens:** Bestelwagens verbruiken ongeveer 11 liter diesel per 100 km (1,1 liter per km), wat gelijkstaat aan 11 kWh/km.
  - **Elektrische voertuigen:** Deze rijden ongeveer 5 km op 1 kWh, wat neerkomt op 0,2 kWh/km.
  - **Personenauto`s:**
    - Benzineauto`s rijden ongeveer 15 km op 1 liter benzine. Eén liter benzine bevat circa 8,9 kWh, wat resulteert in 0,59 kWh/km. Het aandeel benzineauto`s in Nederland is 76,11% (CBS).
    - Dieselauto`s rijden ongeveer 21 km op 1 liter diesel, met een energiewaarde van 10 kWh per liter, wat neerkomt op 0,48 kWh/km. Het aandeel dieselauto`s in Nederland is 8,2% (CBS).

  **Schatting laadtijden:**
  - Laadtijden zijn afhankelijk van de lading, het type voertuig en de sector waarin het bedrijf actief is.

  **Schatting van het aantal voertuigen:**
  - **Vrachtwagens:** Geschat op basis van de behoefte aan transport van grote ladingen, vooral in de voedings- en koeltransportsector.
  - **Bestelwagens:** Geschat voor kleinere leveringen en distributie naar klanten en winkels.
  - **Elektrische voertuigen:** Aangenomen op basis van de trend naar duurzaamheid en de toename van elektrisch vervoer in de sector.
  - **Personenauto`s:** Geschat voor personeel en kleine zakelijke ritten.

  **Elektrificatiegraad:**
  - De elektrificatiegraad groeit lineair tot het jaar 2050.

  **Bronnen:**
  - Transport en Logistiek Nederland (TLN): [tln.nl](https://www.tln.nl)
  - Rijksdienst voor Ondernemend Nederland (RVO): [rvo.nl](https://www.rvo.nl)
  - Sectorrapporten van Panteia en CBS: [cbs.nl](https://www.cbs.nl) en [panteia.nl](https://www.panteia.nl)
  """)

# ======================================================================================================================================================================
#elif blog_post == 'Inforamtie terrein':
# ======================================================================================================================================================================
#elif blog_post == 'Energiebehoefte':
# ======================================================================================================================================================================
#elif blog_post == 'Conclusie/Aanbevelingen':
