import PetriNet as pn

# Item 1: Specialist petri net
print('Item 1: Specialist petri net')
free = pn.Place('free', int(input('Input token for free: ')))
busy = pn.Place('busy')
docu = pn.Place('docu')

start  = pn.Transition('start', [free], [busy])
change = pn.Transition('change', [busy], [docu])
end    = pn.Transition('end', [docu], [free])

petri = pn.PetriNet([start, change, end])

print('Place:')
petri.print_place()
print('Transition:')
petri.print_transition()
print('Reachable markings:')
marking_list = petri.reachable()
print("There are", len(marking_list), "reachable markings")


# Item 2: Patient petri net
print('\nItem 2: Patient petri net')

wait_token = int(input('Input token for wait: '))
while wait_token > 10:
    wait_token = int(input('Number of token in wait must less than or equal to 10! Input again: '))

wait = pn.Place('wait', wait_token)
inside = pn.Place('inside')
done = pn.Place('done')

start  = pn.Transition('start', [wait], [inside])
change = pn.Transition('change', [inside], [done])

petri = pn.PetriNet([start, change])

print('Place:')
petri.print_place()
print('Transition:')
petri.print_transition()
print('Reachable markings:')
marking_list = petri.reachable()
print("There are", len(marking_list), "reachable markings")


# Item 3: Grand petri net
print('\nItem 3: Patient petri net')
wait_token = int(input('Input token for wait: '))
while wait_token > 10:
    wait_token = int(input('Number of token in wait must less than or equal to 10! Input again: '))

wait = pn.Place('wait', wait_token)
free = pn.Place('free', int(input('Input token for free: ')))
busy = pn.Place('busy')
docu = pn.Place('docu')
inside = pn.Place('inside')
done = pn.Place('done')

start  = pn.Transition('start', [free, wait], [busy, inside])
change = pn.Transition('change', [busy, inside], [docu, done])
end    = pn.Transition('end', [docu], [free])

petri = pn.PetriNet([start, change, end])

print('Place:')
petri.print_place()
print('Transition:')
petri.print_transition()
print('Reachable markings:')
marking_list = petri.reachable()
print("There are", len(marking_list), "reachable markings")
