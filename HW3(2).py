firstSide = int(input('please inter first side of tringle:'))
secondSide = int(input('please inter second side of tringle:'))
thirdSide = int(input('please inter third side of tringle:'))


if firstSide + secondSide < thirdSide or firstSide +thirdSide < secondSide or thirdSide + secondSide <firstSide :    
    print('ERROR')
else: 1 == ((firstSide ** 2 ) + (secondSide ** 2)) - (thirdSide ** 2 ) 
2 == ((firstSide ** 2 ) + (thirdSide ** 2 )) - (secondSide ** 2 )
3 == ((thirdSide ** 2 ) + (secondSide ** 2 )) - (firstSide ** 2)
if 1 == 0 or 2 == 0 or 3 == 0 :
    print('RIGHT')
else:
        print('NOT RIGHT')


