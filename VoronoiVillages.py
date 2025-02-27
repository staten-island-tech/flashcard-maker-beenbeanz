def VoronoiVillages(villages):
    neighborhoodSizes = []
    villages.sort()
    villages.remove(villages[0])
    villages.remove(villages[len(villages) - 1])

    for i in range(len(villages) - 1):
        neighborhoodSize = villages[i+1] - villages[i]
        neighborhoodSizes.append(neighborhoodSize)
        
    print(villages)     
    print(min(neighborhoodSizes))
VoronoiVillages([5, 16, 0, 10, 4, 15])
