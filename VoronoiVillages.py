def VoronoiVillages(length, villages):
    neighborhoodSizes = []
    finalListISwear = []
    villages.sort()
    for i in range(0, len(villages) - 1):
        neighborhoodSize = (villages[i+1] - villages[i]) / 2
        neighborhoodSizes.append(neighborhoodSize)
    for i in range(len(neighborhoodSizes) - 1):
        finalListISwear.append(neighborhoodSizes[i] + neighborhoodSizes[i+1])
    return min(finalListISwear)
print(VoronoiVillages(5, [16, 0, 10, 4, 15]))

#[0, 4, 5, 10, 15, 16]
#half the distance bewtween each village