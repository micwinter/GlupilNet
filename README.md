# GlupilNet: A pupil segmentation framework for annotating eyetracking videos. 

Forked from [Ellseg](https://bitbucket.org/RSKothari/ellseg/src/master/) by Rakshit Kothari.
# Annotate pupil locations on eyetracking videos
For quick inference on your own eye videos, please use `evaluate_glupilnet.py` as `python evaluate_glupilnet.py --path2data=${PATH_EYE_VIDEOS} --vid_ext=<VIDEO_EXT> --ellseg_ellipses=1 --save_overlay`. 

This will run the pretrained GlupilNet on the eye videos in the given path and produce eye videos with the extension `'*_glupil.mp4'`, where pupil predictions are shown in the video. In addition, it will also produce a numpy file with pupil coordinate predictions with the extension `'*_pred.npy'`.

Example beginning file structure:
* `${path_eye_videos}`
  * exp_name_0 (can be anything)  
    * eye0.mp4
    * eye1.mp4
  * exp_name_1
    * eye0.mp4

After running `evaluate_glupilnet.py`:
* `${path_eye_videos}`
	* exp_name_0
		* eye0.mp4
		* eye1.mp4
      * eye0_glupil.mp4
      * eye0_pred.npy
      * eye1_glupil.mp4
      * eye1_pred.npy
	* exp_name_1
		* eye0.mp4
      * eye0_glupil.mp4
      * eye0_pred.npy


Note the other flags and their (default values)


* `--vid_ext` (mp4) - Look out for videos with user decided extension
* `--overwrite` (False) - Overwrite existing files
* `--save_overlay` (True) - Save out segmentation output map on eye video, produces video with extension `*_glupil.mp4`
* `--eval_on_cpu` (False) - If no GPU available or found, GlupilNet can also be evaluated using CPU
* `--evaluate_performance` (False) - Load groundtruth pupil coordinates (`*_pupils.npy`) and evaluate GlupilNet performance via euclidean distance. Produces a video with both prediction and groundtruth pupil annotations with the extension `*_glupil_evaluate.mp4`. Will raise error if groundtruth annotations not found, in the form `'* pupils.npy'`.
* `--ellseg_ellipses` (-1) - Use EllSeg proposed ellipses, if FALSE, it will fit an ellipse to segmentation mask.
* `--load_file` (./weights/all.git_ok) - Choose a weight configuration. Default is *all* which was trained on a combination of all available datasets 
* `--check_for_string_in_fname` ('') - Only evaluate on videos with a user defined string. Example `--check_for_string_in_fname=eye` will evaluate on videos with `'eye'` within it


# Citations

If you only use this code base, please cite the following works
EllSeg 
```
@article{kothari2020ellseg,
  title={EllSeg: An Ellipse Segmentation Framework for Robust Gaze Tracking},
  author={Kothari, Rakshit S and Chaudhary, Aayush K and Bailey, Reynold J and Pelz, Jeff B and Diaz, Gabriel J},
  journal={arXiv preprint arXiv:2007.09600},
  year={2020}
}
```
RITEyes
```
@inproceedings{nair2020rit,
  title={RIT-Eyes: Rendering of near-eye images for eye-tracking applications},
  author={Nair, Nitinraj and Kothari, Rakshit and Chaudhary, Aayush K and Yang, Zhizhuo and Diaz, Gabriel J and Pelz, Jeff B and Bailey, Reynold J},
  booktitle={ACM Symposium on Applied Perception 2020},
  pages={1--9},
  year={2020}
}
```
Please cite and credit individual datasets at their own respective links.