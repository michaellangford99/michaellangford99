---
layout: default
title: ME578 Chapter 2
description: Sampling theory, Z-transform, Nyquist

eleventyNavigation:
  key: ch2
  parent: engineering
  title: ME578 Chapter 2

---

Sampling and it's Laplace representation.

**Z-transform derivation**

Define 

$$ x^*(t) = x(t) \cdot \delta_T(t) $$

where 

$$ \delta_T(t) = \sum_{k=-\infty}^{\infty}\delta(t-kT) $$

So

$$x^*(t) = \sum_{k=-\infty}^{\infty}x(t)\delta(t-kT) $$

Laplace transform

$$ X^\*(s) = \mathcal{L}[x^\*(t)] = \int_{-\infty}^{\infty}{x^\*(t)e^{-st}dt}$$

Plug in x*(t):

$$= \int_{-\infty}^{\infty}{\left[\sum_{k=-\infty}^{\infty}x(t)\delta(t-kT)\right]e^{-st}dt}$$

Swap summation and integral

$$= \sum_{k=-\infty}^{\infty}{\int_{-\infty}^{\infty}x(t)\delta(t-kT)e^{-st}dt}$$

$$= \sum_{k=-\infty}^{\infty}{\int_{-\infty}^{\infty}x(t)e^{-st}\delta(t-kT)dt}$$

$$= \sum_{k=-\infty}^{\infty}{x(kT)e^{-skT}}$$

Let

$$ z = e^{Ts}$$

$$ X^\*(z) = \sum_{k=-\infty}^{\infty}{x(kT)z^{-k}} $$

**Impulse train frequency domain representation**

Impulse train is periodic and can be represented as a Fourier series.

$$\delta_T(t) = \sum_{k=-\infty}^{\infty}{\delta(t-kT)} $$

$$\delta_T(t) = \sum_{N=-\infty}^{\infty}{C_Ne^{j\frac{2\pi}{T}Nt}}$$

C_N is:

$$C_N = \frac{1}{T}\int_{-T/2}^{T/2}{\delta_T(t)e^{-j\frac{2\pi Nt}{T}dt}}$$

$$C_N = \frac{1}{T}\int_{-T/2}^{T/2}{\left[\sum_{k=-\infty}^{\infty}{\delta(t-kT)}\right]e^{-j\frac{2\pi Nt}{T}dt}}$$

(Swap)

$$C_N = \frac{1}{T}\sum_{k=-\infty}^{\infty}\int_{-T/2}^{T/2}{\delta(t-kT)}e^{-j\frac{2\pi Nt}{T}dt}$$

$$C_N = \frac{1}{T}\int_{-T/2}^{T/2}{\delta(t)}e^{-j\frac{2\pi Nt}{T}dt}$$

$$C_N = \frac{1}{T}e^{-j\frac{2\pi N*0}{T}dt}$$

$$C_N = \frac{1}{T}e^{0}dt = \frac{1}{T}$$

Therefore

$$\delta_T(t) = \sum_{k=-\infty}^{\infty}{\delta(t-kT)} = \frac{1}{T}\sum_{N=-\infty}^{\infty}{e^{j\frac{2\pi}{T}Nt}}$$

$$w_s = \frac{2\pi}{T}$$

So

$$\delta_T(t) = \sum_{k=-\infty}^{\infty}{\delta(t-kT)} = \frac{1}{T}\sum_{N=-\infty}^{\infty}{e^{jw_sNt}}$$

This demonstrates that a train of impulses in the time domain results in a train of impulses in the frequency domain, with a spacing of 2*pi/T where T is the spacing in the time domain.

So remember-> sampling in the TD <-> replication in the FD, because multiplication int the TD is convolution in the FD. This will be show next.

**Sampling in the frequency domain**

Again:

$$ \delta_T(t) = \sum_{k=-\infty}^{\infty}\delta(t-kT) $$

$$ x^*(t) = x(t) \cdot \delta_T(t) = \sum_{k=-\infty}^{\infty}x(t)\delta(t-kT) $$

$$ X^\*(s) = \mathcal{L}[x^\*(t)] = \int_{-\infty}^{\infty}{x^\*(t)e^{-st}dt}$$

$$ X^\*(s) = \mathcal{L}[x^\*(t)] = \int_{-\infty}^{\infty}{x(t)  \delta_T(t)e^{-st}dt}$$

Pull in frequency domain representation of impulse train:

$$ X^\*(s) = \mathcal{L}[x^\*(t)] = \int_{-\infty}^{\infty}{x(t)  \left[   \frac{1}{T}\sum_{N=-\infty}^{\infty}{e^{jw_sNt}} \right]  e^{-st}dt}$$

$$ X^\*(s) = \frac{1}{T}\sum_{N=-\infty}^{\infty}\int_{-\infty}^{\infty}{x(t) e^{jw_sNt} e^{-st}dt}$$

$$ X^\*(s) = \frac{1}{T}\sum_{N=-\infty}^{\infty}\int_{-\infty}^{\infty}{x(t) e^{-(s - jw_sN)t}dt}$$

This now has the form of a Laplace transform and can be treated as such.

$$ X^\*(s) = \frac{1}{T}\sum_{N=-\infty}^{\infty} X(s - jw_sN)$$

Just look at the frequency spectrum, s = jw:

$$ X^\*(jw) = \frac{1}{T}\sum_{N=-\infty}^{\infty} X(jw - jw_sN)$$

$$ X^\*(jw) = \frac{1}{T}\sum_{N=-\infty}^{\infty} X(j(w - w_sN))$$

So we can see sampling has a gain of 1/T, and has a frequency spectrum with replications at integer multiples of w_s