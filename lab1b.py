def recept(antal):
    f_smor = 2.5 * antal
    strobrod = 0.1875 * antal
    agg = int(0.75 * antal)
    socker = 0.75 * antal
    v_socker = 0.5 * antal
    bakpulver = 0.5 * antal
    v_mjol = 0.75 * antal
    smor = 18.75 * antal
    vatten = 0.25 * antal

    print("Till formen:\nca {0} g smör\nca {1} dl ströbröd\n\nSockerkaka:\n{2} st ägg\n{3} dl strösocker\n{4} tsk vaniljsocker\n\
{5} tsk bakpulver\n{6} dl vetemjöl\n{7} g smör\n{8} dl vatten".format(f_smor,strobrod, agg, socker, v_socker, bakpulver, v_mjol, smor, vatten))


def tidblanda(antal):
    return 10+antal

def tidgradda(antal):
    return 30+(antal*3)

def sockerkaka(antal):
    recept(antal)
    print("\nTidåtgång: ", (tidblanda(antal)+tidgradda(antal))," min\n")
    print("-----------------------------------------------------------------\n")


sockerkaka(4)
sockerkaka(7)
