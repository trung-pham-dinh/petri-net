import PetriNet as pn

free = pn.Place('free',1)
wait = pn.Place('wait',3)
busy = pn.Place('busy')
insd = pn.Place('inside')
docu = pn.Place('docu')
done = pn.Place('done',1)

start  = pn.Transition('start', [free, wait], [busy, insd])
change = pn.Transition('change', [busy, insd], [docu, done])
end    = pn.Transition('end', [docu], [free])

petri = pn.PetriNet([start, change, end])

print("Initial")
petri.print_place()
petri.print_transition()
petri.print_marking()

# print("Run")
# petri.run([start, change, end])
# petri.print_marking()

print("Reaachable")
petri.reachable() # Question 4


