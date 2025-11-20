import matplotlib.pyplot as plt
import spelunker


spk2 = spelunker.load('/Users/sebastianzieba/Desktop/Projects/Open_Source/fomo/tmp', pid=7675)
spk2.mast_api_token = 'enter_mast_token_id_here' # input mast_api token here!

fig, ax = plt.subplots(figsize=(12,4),dpi=200)

ax = spk2.mnemonics_local('GUIDESTAR') # plots when the JWST tracks onto a new guidestars as a vertical line
ax = spk2.mnemonics('SA_ZHGAUPST') # plots the start and end of high gain antenna movement

ax.plot(spk2.fg_time, spk2.fg_flux)
plt.legend(loc=3)

plt.xlim(60067.84, 60067.9)