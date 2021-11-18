import PetriNet as pn

free = pn.Place(1)
wait = pn.Place(3)
busy = pn.Place()
insd = pn.Place()
docu = pn.Place()
done = pn.Place(1)

start  = pn.Transition([free, wait], [busy, insd])
change = pn.Transition([busy, insd], [docu, done])
end    = pn.Transition([docu], [free])

petri = pn.PetriNet([start, change, end])

