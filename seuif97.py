I=[0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,4,5,8,8,21,23,29,30,31,32]
J=[-2,-1,0,1,2,3,4,5,-9,-7,-1,0,1,3,-3,0,1,3,17,-4,0,6,-5,-2,10,-8,-11,-6,-29,-31,-38,-39,-40,-41]
N=[0.14632971213167,-0.84548187169114,-3.7563603672040,3.3855169168385,-0.95791963387872,0.15772038513228,-0.016616417199501,0.00081214629983568,0.00028319080123804,-0.00060706301565874,-0.018990068218419,-0.032529748770505,-0.021841717175414,-0.000052838357969930,-0.00047184321073267,-0.00030001780793026,0.000047661393906987,-0.0000044141845330846,-0.00000000000000072694996297594,-0.000031679644845054,-0.0000028270797985312,-0.00000000085205128120103,-0.0000022425281908000,-0.00000065171222895601,-0.00000000000014341729937924,-0.00000040516996860117,-0.0000000012734301741641,-0.00000000017424871230634,-0.00000000000000000068762131295531,0.000000000000000000014478307828521,0.000000000000000000000026335781662795,-0.000000000000000000000011947622640071,0.0000000000000000000000018228094581404,-0.000000000000000000000000093537087292458]
P1 = 16.53
T1 = 1386
R1 = 0.461526

def gamma(p, t):
    pi = p / P1
    tau = T1 / t
    sum = 0
    for i in range(1, 35):
        sum += N[i - 1] * (7.1 - pi)**I[i - 1] * (tau - 1.222)**J[i - 1]
    return sum


def gammapi(p, t):
    pi = p / P1
    tau = T1 / t
    sum = 0
    for i in range(1, 35):
        sum -= N[i - 1] * I[i - 1] * (7.1 - pi)**(I[i - 1] - 1) * (tau - 1.222)**J[i - 1]
    return sum


def gammapipi(p, t):
    pi = p / P1
    tau = T1 / t
    sum = 0
    for i in range(1, 35):
        sum += N[i - 1] * I[i - 1] * (I[i - 1] - 1) * (7.1 - pi)**(I[i - 1] - 2) * (tau - 1.222)**J[i - 1]
    return sum


def gammatau(p, t):
    pi = p / P1
    tau = T1 / t
    sum = 0
    for i in range(1, 35):
        sum += N[i - 1] * (7.1 - pi)**I[i - 1] * J[i - 1] * (tau - 1.222)**(J[i - 1] - 1)
    return sum


def gammatautau(p, t):
    pi = p / P1
    tau = T1 / t
    sum = 0
    for i in range(1, 35):
        sum += N[i - 1] * (7.1 - pi)**I[i - 1] * J[i - 1] * (J[i - 1] - 1) * (tau - 1.222)**(J[i - 1] - 2)
    return sum


def gammapitau(p, t):
    pi = p / P1
    tau = T1 / t
    sum = 0
    for i in range(1, 35):
        sum -= N[i - 1] * I[i - 1] * (7.1 - pi)**(I[i - 1] - 1) * J[i - 1] * (tau - 1.222)**(J[i - 1] - 1)
    return sum


def specific_volume(p, t):
    pi = p / P1
    volume = pi * gammapi(p, t) * R1 * t / (p * 1000)
    return volume


def specific_internal_energy(p, t):
    pi = p / P1
    tau = T1 / t
    energy = (tau * gammatau(p, t) - pi * gammapi(p, t)) * R1 * t
    return energy


def specific_entropy(p, t):
    tau = T1 / t
    entropy = (tau * gammatau(p, t) - gamma(p, t)) * R1
    return entropy


def specific_enthalpy(p, t):
    tau = T1 / t
    enthaply = tau * gammatau(p, t) * R1 * t
    return enthaply


def specific_isobaric_heat_capacity(p, t):
    tau = T1 / t
    capacity = 0 - tau**2 * gammatautau(p, t) * R1
    return capacity


def specific_isochoric_heat_capacity(p, t):
    tau = T1 / t
    s1 = gammapi(p, t) - tau * gammapitau(p, t)
    s2 = s1 * s1 / gammapipi(p, t)
    capacity = specific_isobaric_heat_capacity(p, t) + s2
    return s2


def speed_of_sound(p, t):
    tau = T1 / t
    s1 = gammapi(p, t)**2
    s2 = gammapi(p, t) - tau * gammapitau(p, t)
    s3 = s2**2
    s4 = tau**2 * gammatautau(p, t)
    s5 = s3 / s4
    speed = (s1 * R1 * t * 1000 / (s5 - gammapipi(p, t)))**0.5
    return speed


def backward_equations(h, s):
    p1 = 100
    h1 = 3400
    s1 = 7.6
    eta = h / h1
    sigma = s / s1
    sum = 0
    I=[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,3,4,4,5]
    J=[0,1,2,4,5,6,8,14,0,1,4,6,0,1,10,4,1,4,0]
    n=[-0.691997014660582,-0.183612548787560e2,-9.28332409297335,0.659639569909906e2,-0.162060388912024e2,0.450620017338667e3,0.854680678224170e3,0.607523214001162e4,0.326487682621856e2,-0.269408844582931e2,-0.319947848334300e3,-0.928354307043320e3,0.303634537455249e2,-0.650540422444146e2,-0.430991316516130e4,-0.747512324096068e3,0.730000345529245e3,0.114284032569021e4,-0.436407041874559e3]
    for i in range(0,19):
        sum += n[i] * (eta + 0.05) ** I[i] * (sigma + 0.05) ** J[i]
    p = sum * p1
    return p

       
    
    
    
    
        
        
