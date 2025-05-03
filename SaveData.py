import csv

def save_data(times, exposures): # creates a new file for writing later
    with open('exposure_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

    
        header = ['Time'] # writing the headings
        for i in range(len(exposures)):
            header.append(f'Particle_{i+1}')
        writer.writerow(header)

    
        for i in range(len(times)): # write the data for each time steps
            row = [times[i]]
            for p in exposures:
                row.append(p[i])
            writer.writerow(row)

    print("Saved to exposure_data.csv")
