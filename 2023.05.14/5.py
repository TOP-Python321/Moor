def central_tendency(*sample: tuple) -> dict[str, float]:
    """
    Returns a dictionary with computed central trend measure values
    """
    length_of_tuple = len(sample)
    index = length_of_tuple // 2
    arithmetic = sum(sample) / length_of_tuple
    multiplied = 1
    numerator_sum = 0
    
    if length_of_tuple % 2:
        median = float(sorted(sample)[index])
    else:
        median = sum(sorted(sample)[index - 1:index + 1]) / 2
        
    for i in sample:
        multiplied *= i 
        numerator_sum += 1 / i
    geometric = multiplied ** (1/length_of_tuple)
    harmonic = length_of_tuple / numerator_sum
    
    tendency = {
                'median': median,
                'arithmetic': arithmetic,
                'geometric': geometric,
                'harmonic': harmonic
                }
                
    return tendency
    
    
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>> central_tendency(1, 2, 3, 4, 56, 10, 5)
# {'median': 4, 'arithmetic': 11.571428571428571, 'geometric': 4.8935517101149655, 'harmonic': 2.915220624690134}
# >>> central_tendency(1, 2, 3, 4, 56, 10, 5, 8)
# {'median': 4.5, 'arithmetic': 11.125, 'geometric': 5.203641966051238, 'harmonic': 3.166823751178134}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}