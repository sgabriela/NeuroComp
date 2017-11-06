#importando biblioteca brian
from brian2 import*
from matplotlib import*

#definindo constantes
tau = 20*ms
vrest = -60.0*mV
R = 100*Mohm
eqs = '''
    dv/dt = (-(v-vrest) + R*I)/tau:volt
    I = 0.25*nA*(t>=50*ms) - 0.25*nA*(t>=250*ms):amp
'''

#criando grupo com n=1 neurônio, com as propriedades abaixo 
neuron = NeuronGroup(1, eqs, threshold= 'v> -50.0*mV', reset = 'v = vrest', refractory = 5*ms, method = 'euler')

#neurônio sendo inicializado com o valor de repouso
neuron.v = vrest

#gravando as variáveis 'V'(voltagem) e 'I' (corrente)
state_m = StateMonitor(neuron, 'v', record = True)
state_i = StateMonitor(neuron, 'I', record = True)

#gravando os spikes
spike_mon = SpikeMonitor(neuron)

#roda a simulação
run (500*ms, report= 'stdout')

subplot(211)
plot(state_m.t/ms, state_m.v[0]/mV)
xlabel('Tempo')
ylabel('Voltagem')

subplot(212)
plot(state_m.t/ms, state_i.I[0]/nA)
xlabel('Tempo')
ylabel('Corrente')

print("Nro disparos = ", spike_mon.count[0])
 
#frequência = qtd disparos/tempo de aplicação da corrente
freq = (spike_mon.count[0]/200)*Hz

print("Frequencia disparos do neuronio = ", freq)
show()


