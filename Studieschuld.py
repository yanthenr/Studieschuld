import matplotlib.pyplot as plt

minimumloon = 1934.40 # per maand
rente = 2.56

def Studieschuld(schuld: float, loon: float, alleenstaand: bool, kinderen: bool, partnerloon = 0):
    """
    Je aflosfase is maximaal 35 jaar.
    Er wordt standaard rekening gehouden met je draagkracht.
    Van je inkomen wordt een draagkrachtvrije voet afgehaald. 
    Het inkomen van je partner telt altijd mee bij de berekening van je draagkracht.
    Je hoeft nooit meer dan 4% van je inkomen boven de draagkrachtvrije voet te betalen.
    De draagkrachtvrije voet is een percentage van het minimumloon en is afhankelijk
    van je persoonlijke situatie. Ben je alleenstaand zonder kinderen, dan is de
    draagkrachtvrije voet 100% van het minimumloon. In alle andere gevallen is het 143%.

    Bij minimaal 5 euro per maand terug betalen

    Rente is op jaarbasis


    """
    inkomen = loon
    beginschuld = schuld

    # Bent u alleenstaand zonder kinderen, dan is de draagkrachtvrije voet 100% van het minimumloon.
    # # In alle andere gevallen is het 143%.

    if (alleenstaand and not kinderen): 
        draagkrachtvrijevoet = 1
    else: 
        draagkrachtvrijevoet = 1.43
        if (not alleenstaand):
            inkomen += partnerloon

    draagkrachtvrijevoet = draagkrachtvrijevoet * minimumloon

    # U hoeft nooit meer dan 4% van uw inkomen boven de draagkrachtvrije voet te betalen. 
    draagkracht = 0.04 * (inkomen - draagkrachtvrijevoet)

    # U betaalt pas terug als uw draagkracht hoger is dan € 5,- per maand. Is het lager, dan hoeft u niet te betalen.
    if draagkracht < 5:
        draagkracht = 0

    studieschuld = []
    afbetaald = []
    renteloos = []
    betaald = 0

    for jaar in range(1,36):
        jaarrente = schuld * (rente/100)
        schuld += jaarrente
        
        for maand in range(1,13):
            if schuld > 0:
                schuld = schuld - draagkracht
                studieschuld.append(schuld)

                betaald += draagkracht
                afbetaald.append(betaald)
                renteloos.append(beginschuld-betaald)


    y = list(range(1,len(studieschuld)+1))

    plt.figure(figsize=(10,5))
    plt.title("Studieschuld van "+str(beginschuld)+" met maandelijks inkomen van "+str(inkomen)+", "+str(draagkracht)+" draagkracht")

    # Plots
    plt.plot(y, studieschuld, color='red', label='studieschuld')
    plt.plot(y, afbetaald, color='green', label='afbetaald')
    plt.plot(y, renteloos, color='blue', label='renteloze schuld')

    # Ticks als jaar
    aantaljaar =  [j for j in y if j % 12 == 0]
    plt.xticks(aantaljaar, list(range(1,len(aantaljaar)+1)))
    plt.xlabel('Jaar')
    plt.ylabel('€')
    plt.ylim(0, max(studieschuld))
    plt.legend()
    plt.show()

    return schuld

# Voorbeeld van een schuld van 90.000, maandelijkse inkomsten 3000, alleenstaand zonder kinderen
bereken = Studieschuld(90000, 3000, True, False)
print(bereken)