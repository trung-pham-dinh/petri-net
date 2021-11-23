import PetriNet as pn

free = pn.Place('free',3)
wait = pn.Place('wait',10)
busy = pn.Place('busy')
insd = pn.Place('inside')
docu = pn.Place('docu')
done = pn.Place('done',1)

start  = pn.Transition('start', [free, wait], [busy, insd])
change = pn.Transition('change', [busy, insd], [docu, done])
end    = pn.Transition('end', [docu], [free])

# this case for test the reachable marking if the petri have no deadlock
# start  = pn.Transition('start', [free], [busy])
# change = pn.Transition('change', [busy], [docu])
# end    = pn.Transition('end', [docu], [free])

petri = pn.PetriNet([start, change, end])

print("Initial")
petri.print_place()
petri.print_transition()
petri.print_marking()

# print("Run")
# petri.run([start, change, end])
# petri.print_marking()

print("Reaachable")
marking_list = petri.reachable() # Question 4

print("There are", len(marking_list), "reachable markings")
