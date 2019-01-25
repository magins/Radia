from . import plumbing as _radia

__all__ = ['magnetic', 'steel']

# Magnetic materials
class magnetic(object):
    NdFeB = _radia.MatLin([0.06, 0.17], 1.2)
    SmCo5 = _radia.MatLin([0.005, 0.04], 0.85)
    Sm2Co17 = _radia.MatLin([0.005, 0.04], 1.05)
    Ferrite = _radia.MatLin([0.07, 0.2], 0.35)


# Steel materials
class steel(object):
    Xc06 = _radia.MatSatIsoFrm([1.3620, 2118.0],
                               [0.2605, 63.060],
                               [0.4917, 17.138])

    Steel37 = _radia.MatSatIsoFrm([1.1488, 1596.3],
                                  [0.4268, 133.11],
                                  [0.4759, 18.713])

    Steel42 = _radia.MatSatIsoFrm([1.441, 968.66],
                                  [0.2912, 24.65],
                                  [0.3316, 8.300])

    AFK502 = _radia.MatSatIsoFrm([1.788, 10485.0],
                                 [0.437, 241.500],
                                 [0.115, 7.43000])

    AFK1 = _radia.MatSatIsoFrm([1.704, 2001.0],
                               [0.493, 38.560],
                               [0.152, 1.2400])

iron = _radia.MatSatIsoFrm([20000, 2.0],
                           [0.100, 2.0],
                           [0.100, 2.0])

