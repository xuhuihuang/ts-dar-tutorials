If running on command line:

run the following:
ipython
%run -i 1_ContourPlot2D.py
%run -i 2_load_data.py
%run -i 3_create_2Dplot.py
%run -i 4_train.py
%run -i 5_validation_loss.py
%run -i 6_dispersion_loss.py
%run -i 7_compute_OOD_scores.py
%run -i 8_plot_4state_model.py

NOTE:
(A) %run -i 3_create_2Dplot.py will output:
	(1) free_energy_2d.png

(B) %run -i 4_train.py will output:
	(1) validation_vamp.npy
	(2) validation_dis.npy
	(3) validation_prototypes.npy
	(4) training_vamp.npy
	(5) training_dis.npy
	(6) hypersphere_embs.npy
	(7) metastable_states.npy
	(8) ood_scores.npy
	(9) state_centers.npy
	(10) model.pt

(C) %run -i 5_validation_loss.py will output:
	(1) validation_vamp.png

(D) %run -i 6_dispersion_loss.py will output:
	(1) dispersion_loss.png 

(E) %run -i 8_plot_4state_model.py will output:
	(1) 4state_free_energy_landscape.png
	(2) 4state_hypersphere.png
