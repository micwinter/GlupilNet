from utils import export_to_onnx

loadfile = "/home/jlg/michele/gbox/projects/GlupilNet/weights/all.git_ok"
outpath = "/media/bigger_hdd/GlupilNet_data/glupilnet_{:%Y-%b-%d_%H:%M:-S}.onnx"


export_to_onnx(
    loadfile,
    model_dict_key="ritnet_v3",
    eval_on_cpu=False,
    output_path="glupilnet_{:%Y-%b-%d_%H:%M:-S}.onnx",
    verbose=True,
    input_names=None,
    output_names=None,
)

