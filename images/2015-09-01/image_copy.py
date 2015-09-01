#!/usr/bin/python

import os

images = [

'/d/bip3/ezbc/multicloud/figures/av/perseus_*vs*.png',
'/d/bip3/ezbc/multicloud/figures/spectra/multicloud_spectra.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/multicloud_av_vs_nhi.png',
'/d/bip3/ezbc/multicloud/figures/av_nhi/multicloud_av_vs_nhi_scatter.png',

        ]

'''
# int, planck
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_binned_coarseres_likelihood_w?.png',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_planck_binned_coarseres_likelihood_w?.png',
'/d/bip3/ezbc/california/figures/likelihood/california_planck_binned_coarseres_likelihood_w?.png',

# no int, planck
'/d/bip3/ezbc/perseus/figures/likelihood/perseus_planck_binned_coarseres_noint_likelihood_w?.png',
'/d/bip3/ezbc/taurus/figures/likelihood/taurus_planck_binned_coarseres_noint_likelihood_w?.png',
'/d/bip3/ezbc/california/figures/likelihood/california_planck_binned_coarseres_noint_likelihood_w?.png',


'/d/bip3/ezbc/perseus/figures/likelihood/perseus_lee12_binned_coarseres_fixedwidth_likelihood_di.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_fixedwidth_av_vs_nhi*.png',
'/d/bip3/ezbc/perseus/figures/diagnostics/perseus_lee12_binned_coarseres_fixedwidth_nh2_vs_nhi*png',
'''

dest_dir = './'

for image in images:
    os.system('cp ' + image + ' ' + dest_dir)

