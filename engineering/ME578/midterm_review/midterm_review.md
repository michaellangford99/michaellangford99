---
layout: default
title: ME578 Midterm Review
description: Z-transform review, ZOH, State-space, etc.

eleventyNavigation:
  key: midterm_review
  parent: engineering
  title: ME578 Midterm Review

---

# Table of Contents

- Z-transform review
- ZOH
- State-space
- Controllability/Observability

**Z transform of time advance**

$$Z[x[k+d]] = z^d \left[X(z) - \sum_{j=0}^{d-1}x[j]z^{-j}\right]$$

Proof:

$$Z[x[k+d]] = \sum_{k=0}^\infty x[k+d]z^{-k}$$

Change of variable

$$j = k+d$$
$$k = j-d$$

Substitute

$$ = \sum_{j=d}^{\infty}x[j]z^{-(j-d)}$$

$$ = z^d \sum_{j=d}^{\infty}x[j]z^{-j}$$

$$ = z^d \left[ \sum_{j=0}^{\infty}x[j]z^{-j} - \sum_{j=0}^{d-1}x[j]z^{-j} \right]$$

$$Z[x[k+d]] = z^d \left[ X(z)- \sum_{j=0}^{d-1}x[j]z^{-j} \right]$$


**Impulse Sampled System**

Recall:

$$x^*(t) = \sum_{k=-\infty}^{\infty}x(t)\delta(t-kT) = \sum_{k=-\infty}^{\infty}x(kT)\delta(t-kT)$$

$$X^\*(s) = \mathcal{L}[x^\*(t)] = \int_{0}^{\infty} x^\*(\tau) \cdot e^{-s\tau}d\tau = \sum_{k=0}^{\infty} x(kT) \cdot e^{-kTs}$$

Assume a LTI system X is followed by a sampler, and fed to another LTI system G

$$Y(s) = G(s) \cdot X^*(s)$$

Now if this resulting system is sampled:

$$Y^\*(s) = \left[G(s) \cdot X^*(s)\right]^\*$$

**The X\*(t) may be factored out**

$$Y^\*(s) = G^\*(s) \cdot X^\*(s)$$

Proof:
$$y(t) = \int_{0}^{t}g(t-\tau) \cdot x^\*(\tau)d\tau$$

$$ = \int_{0}^{t}g(t-\tau) \cdot \sum_{k=0}^{\infty}x(\tau)\delta(\tau - kT)d\tau
= \sum_{k=0}^{\infty}\int_{0}^{t}g(t-\tau)x(\tau) \cdot \delta(\tau - kT)d\tau$$

$$= \sum_{k=0}^{\infty}g(t-kT)\cdot x(kT)$$

Take Z transform of y(t)

$$Y(z) = \mathcal{Z} [y(t)] = \sum_{n=0}^{\infty} \left[ \sum_{k=0}^{\infty}g(t-kT)\cdot x(kT) \right] \cdot z^{-n}$$

Because signals are causal, we can trim the range of integration

$$Y(z) = \mathcal{Z} [y(t)] = \sum_{n=0}^{\infty} \left[ \sum_{k=0}^{n}g(t-kT)\cdot x(kT) \right] \cdot z^{-n}$$

Swap integration order (select limits based on argument of g(.))

$$= \sum_{k=0}^{\infty} \sum_{n=k}^{\infty} g(nT - kT) \cdot x(kT) \cdot z^{-n}$$

Change of variable

$$m = n-k$$

$$= \sum_{k=0}^{\infty} \sum_{m=0}^{\infty} g(mT) \cdot x(kT) \cdot z^{-(m+k)}$$

Summations are now separable

$$= \left[ \sum_{m=0}^{\infty} g(mT)\cdot z^{-m} \right] \cdot \left[\sum_{k=0}^{\infty} x(kT) \cdot z^{-k} \right] = G(z) \cdot X(z)$$

Equivalent to

$$ Y^\*(s) = G^\*(s) \cdot X^\*(s)$$

**Zero-order-hold derivation**

The impulse response of a ZOH transfer function is simply a gate function, with amplitude 1 and duration $T$

Thus the transfer function can be described as

$$g_{zoh}(t) = u(t) - u(t-T)$$

$$G_{ZOH}(s) = \frac{1}{s} - \frac{1}{s}e^{-sT} = \frac{1 - e^{-sT}}{s}$$

**Computing Pulse Transfer Function**

Example

$$G(s) = \frac{1}{s(s+1)}$$

G(s) is fed by a ZOH system fed by a sampled LTI system X*(s)
Since the input is a sampled system, the resulting transfer function can be represented in the Z domain (as we assume that it is also followed by a sampler). I.e. Gtotal(z) = Z[G(s)*Gzoh(s)].

$$G(z) = \mathcal{Z} \left[ G(s) \cdot G_{ZOH}(s) \right]$$

We pull out the $1 - e^{-sT}$ and divide the original TF by s. This makes sense if you think about 1/s.

$$=\mathcal{Z}\left[ \frac{1- e^{-sT}}{s} \frac{1}{s(s+1)} \right] = \mathcal{Z} \left[ (1-e^{-sT}) \frac{1}{s^2(s+1)} \right]$$

$$ (1-z^{-1}) \mathcal{Z} \left[ \frac{1}{s^2(s+1)} \right]$$

$$ \left(\frac{z-1}{z}\right) \mathcal{Z} \left[ \frac{1}{s^2(s+1)} \right]$$

Continue by partial fraction expansion and table method of Z transforms to complete the Z transform

**Non-integer sample time delay**

Example transfer function

$$G_p(s) = \frac{e^{-05s}}{s+1}$$

Fed to ZOH sampler with time period T= 0.2.

$$T_D = nT + T_L$$

$T_D = 0.5$, so n=2, and $T_L = 0.1$

$$G(z) = (1 - z^{-1}) \cdot z^{-2} \cdot \mathcal{Z}\left[ \frac{e^{-05s}}{s(s+1)} \right]$$

$$G(z) = \left(\frac{z-1}{z}\right) \cdot z^{-2} \cdot \mathcal{Z}\left[ \frac{e^{-05s}}{s(s+1)} \right]$$

$$G(z) = \left(\frac{z-1}{z^3}\right) \cdot \mathcal{Z}\left[e^{-05s} \left(\frac{1}{s}-\frac{1}{s-1}\right) \right]$$

The key now is that the continuous time signals have been shifted, and so the sample points now hit different points of the CT function. So you have to then find what the DT equivalent of the sampled signal ends up being.

**State Space**

Continuous-time representation:

$$\dot x(t) = F \cdot x(t) + G \cdot u(t)$$

$$y(t) = C \cdot x(t) + D \cdot u(t)$$

Discrete-time representation:

$$x[k+1] = A \cdot x[k] + B\cdot u[k]$$

$$y[k] = C \cdot x[k] + D \cdot u[k]$$

- State equation - relates new state to previous state and input
- Output equation - relates output to current state and input

Dimensionality convention:
- n states
- r inputs
- m outputs

**State Transition Matrix**

The state transition matrix Phi(t) of a system is an nxn matrix that satisfies the homogeneous (0 input) state equations. So for CT systems:

$$\frac{d}{dt}\Phi(t) = F\cdot \Phi(t)$$

For x(0) as I.C., x(t) is computed as:

$$x(t) = \Phi(t) \cdot x(0)$$

**Definition**

$$\Phi(t) = \mathcal{L}^{-1}\left[(s I - F)^{-1} \right] = e^{Ft}$$

Proof:

$$\frac{d}{dt}\Phi(t) = F\cdot \Phi(t)$$

Take Laplace transform

$$sX(s) - x(0)= F \cdot X(s)$$
$$sX(s) - F \cdot X(s) = x(0)$$
$$(sI - F) \cdot X(s) = x(0)$$
$$X(s) = (sI - F)^{-1} \cdot x(0)$$
$$x(t) = \mathcal{L}^{-1}\left[ (sI - F)^{-1} \cdot x(0) \right]$$
$$x(t) = \mathcal{L}^{-1}\left[ (sI - F)^{-1}\right] \cdot x(0) $$

Which proves the first part of the conjecture. However even though it's obvious an exponential is the solution to the 1st order ODE, we gotta show that this Phi(t) thing does actually solve it.

However I don't feel like writing it out, so I'll just say it's a taylor series expansion that we then take the derivative of via matrix derivative rules and then show it satisfies the ODE.

State transition matrix satisfies following properties:
1. $$ \Phi(0) = I$$
2. $$ \Phi^{-1}(t) = \Phi(-t) $$
3. $$ \Phi(t_1 + t_2) = \Phi(t_1) \cdot \Phi(t_2) = \Phi(t_2) \cdot \Phi(t_1)$$
4. $$ \Phi(t_2 - t_0) = \Phi(t_2 - t_1) \cdot \Phi(t_1 - t_0)$$

Really all just stems from the fact that these are all 1st order ODEs chained together beautifully.

**Example**

$$
\begin{bmatrix} \dot x_1 \newline \dot x_2 \end{bmatrix} = 
\begin{bmatrix}
0 & 1 \newline -2 & -3
\end{bmatrix}
\begin{bmatrix} x_1 \newline x_2 \end{bmatrix}$$

$$F = 
\begin{bmatrix}
0 & 1 \newline -2 & -3
\end{bmatrix}$$

$$\Phi(t) = \mathcal{L}^{-1}\left[ (sI - F)^{-1} \right] = e^{Ft}$$

The e^Ft comes in important at the end!

$$sI - F = 
\begin{bmatrix}
s & -1 \newline 2 & s+3
\end{bmatrix}$$

Invert

$$(sI - F)^{-1} = \frac{1}{(s+3)(s) - (-2)(1)} Adj
\begin{bmatrix}
s & -1 \newline 2 & s+3
\end{bmatrix}$$

$$= \frac{1}{s^2 + 3s + 2}
\begin{bmatrix}
s+3 & 1 \newline -2 & s
\end{bmatrix}$$

Now we can directly take the inverse Laplace transform of the matrix members

$$\Phi(t) = \mathcal{L}^{-1}[(sI - F)^{-1}]$$

For this problem the result is reached via table lookup. I hope.

**Similarity Transform**

State-space representations are non-unique. Any non-singular transformation of the state is allowable.

$$x_{new} = Tx$$

The rest are easy to figure out but this one is the key:

$$ \dot x_{new} = T\dot x = T(Fx(t) + Gu(t)) = TFT^{-1}x_{new}(t) + TGu(t)$$

**Solution of forced response**

Incorporating the input signal, we get multiplication of state transition matrix and input, i.e. convolution, which makes sense.

$$X(s) = (sI - F)^{-1} \cdot x(0) + (sI-F)^{-1} G \cdot U(s)$$

$$x(t) = \Phi(t) \cdot x(0) + \int_0^t \Phi(t-\tau)G\cdot u(\tau)d\tau$$

You could also multiply in the s domain and then find the inverse Laplace transform.

**DT ZOH equivalent representation**

Now assume a system evolving as described by the CT state-space equations is preceded by a ZOH and the output sampled at the same sample period T, in sync.

$$u[k] -> ZOH -> u(t) -> SYSTEM -> y(t) -> sample_T -> y[k]$$

Output equations are valid at sample instants:

$$Y[k] = C \cdot x[k] + D \cdot u[k]$$

Must then find the state transformation relation. Use 2 sample time instants:

$$t = (k+1)T, t_0 = kT$$

Using x(kT) as the I.C. for the state transformation

$$x((k+1)T) = e^{FT} \cdot x(kT) + \int_{kT}^{(k+1)T}e^{F((k+1)T-\tau)}G \cdot u(\tau)d\tau$$

Since due to the ZOH on the input signal, it is constant over the integration period. Thus it can be pulled out of the integral. (It holds the value from kT all the way to at (k+1)T)

$$x((k+1)T) = e^{FT} \cdot x(kT) + \left[\int_{kT}^{(k+1)T}e^{F((k+1)T-\tau)}d\tau \right] G \cdot u(kT)$$

Now a change of variable (yay)

$$\eta = (k+1)T - \tau$$

$$x((k+1)T) = e^{FT} \cdot x(kT) + \left[\int_{0}^{T}e^{F\eta}d\eta \right] G \cdot u(kT)$$

This then yields the ZOH equivalent DT state space representation

$$x[k+1] = A \cdot x[k] + B \cdot u[k]$$
$$y[k] = C \cdot x[k] + D \cdot u[k]$$

Thus

$$A(T) = e^{FT} = \Phi(T)$$
$$B(T) = \left[\int_{0}^{T}e^{F\eta}d\eta \right]G = \int_0^T\Phi(\eta)d\eta \cdot G$$

And if F is nonsingular it can be represented as

$$B(T) = \left[\int_{0}^{T}e^{F\eta}d\eta \right]G = F^{-1}(e^{FT}-I)G$$

**Example**

$$F = 
\begin{bmatrix}
0 & 1 \newline 0 & 0
\end{bmatrix}, 
G = 
\begin{bmatrix}
0 \newline 1
\end{bmatrix}, 
C = 
\begin{bmatrix}
1 & 0
\end{bmatrix}, 
D = 0
$$

First find Phi(t)

$$
\Phi(t) = \mathcal{L}^{-1}\left[(sI - F)^{-1}\right] = \mathcal{L}^{-1}
\begin{bmatrix}
1/s & 1/s^2 \newline
0 & 1/s
\end{bmatrix} =
\begin{bmatrix}
1 & t
\newline
0 & 1
\end{bmatrix}$$

Find A

$$A = \Phi(T) = 
\begin{bmatrix}
1 & T
\newline
0 & 1
\end{bmatrix}
$$

B matrix solution:

$$B = \int_0^T e^{F\eta}d\eta \cdot G = \int_0^T\Phi(\eta)d\eta \cdot G = 
\begin{bmatrix}
\eta & \eta^2/2
\newline
0 & \eta
\end{bmatrix}_0^T \cdot G$$

$$ = \begin{bmatrix}
T & T^2/2 \newline
0 & T
\end{bmatrix} 
\begin{bmatrix}
0 \newline
1
\end{bmatrix} =  
\begin{bmatrix}
T^2/2 \newline
T
\end{bmatrix}
$$

**DT State Space equations**

$$x[k+1] = A \cdot x[k] + B \cdot u[k]$$
$$y[k] = C \cdot x[k] + D \cdot u[k]$$

Solution:

$$x[k] = A^k \cdot x[0] + \sum_{j=0}^{k-1}A^{k-j-1}Bu[j]$$

**Z-transform approach**

$$zX(z) -zx[0] = A \cdot X(z) + B \cdot U(z)$$
$$(zI-A)X(z) = zx[0] + B\cdot U(z)$$

Invert

$$X(z) = (zI - A)^{-1}z\cdot x[0] + (zI-A)^{-1}B \cdot U(z)$$

Inverse Z-transform

$$x[k] = \mathcal{Z}^{-1} \left[X(z)\right] = \mathcal{Z}^{-1} \left[(zI - A)^{-1}z\right]\cdot x[0] + \mathcal{Z}^{-1} \left[(zI-A)^{-1}B\right]\cdot U(z)$$

**Discrete State Transition Matrix**

