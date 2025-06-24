def find_s_algorithm(training_data):
   
    num_attributes = len(training_data[0]) - 1

   
    hypothesis = ['0'] * num_attributes

    
    for example in training_data:
        if example[-1].lower() == 'yes': 
            for i in range(num_attributes):
                if hypothesis[i] == '0':
                    hypothesis[i] = example[i]
                elif hypothesis[i] != example[i]:
                    hypothesis[i] = '?'
    return hypothesis
training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Run FIND-S
hypothesis = find_s_algorithm(training_data)
print("Most specific hypothesis:", hypothesis)
