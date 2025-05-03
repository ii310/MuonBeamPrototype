data = readtable('exposure_data.csv'); % reads the data
time = data.Time;

% creates a graph
figure
plot(time, data.P1, 'r') % 1. red particle
hold on
plot(time, data.P2, 'g') % 1. green particle
plot(time, data.P3, 'b') % 2. blue particle
plot(time, data.P4, 'k') % 3. black particle

xlabel('Time (s)')
ylabel('Magnetic Exposure (s)')
title('Particles in Magnetic Field')
legend('P1', 'P2', 'P3', 'P4')
grid on
