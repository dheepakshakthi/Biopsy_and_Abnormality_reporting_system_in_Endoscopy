thanks to [datasets.simula.no](https://datasets.simula.no/) for biopsy instruments, anatomical landmarks and polyps dataset <br>datasets available at [datasets.simula.no/kvasir-instrument](https://datasets.simula.no/kvasir-instrument/), [datasets.simula.no/kvasir-SEG](https://datasets.simula.no/kvasir-seg/) and [datasets.simula.no/hyper-kvasir](https://datasets.simula.no/hyper-kvasir/)

<h2>About the program </h2> 
This program detects the biopsy instruments to check whether the biopsy is being taken or not. <br>
For double biopsy situations, when the first the first biopsy is finished, the instrument is taken away from the camera... it waits for the threshold frames to complete (frames without the biopsy instrument). <br> If the  instrument comes before the camera after the threshold frames, it detects the instrument and reports it as a second biopsy. 
<br><br>

For the detection, i have used [yolo11](https://docs.ultralytics.com/models/yolo11/#supported-tasks-and-modes) and this model is only trained with 250 images due to insufficient favorable data... but it does detect the instruments well. The trained model is available in the "yolo11_instruments_without_pipe_results" under weights folder. If having sufficient data, it is recommended to go for detection-transformer models such as rt-detr.
<br>
<br>
<b>
I am curently working on classification of anatomical landmarks, detection of polyps and a interface the for managing the report. source code for them will be updated soon! </b>

<h2>Requirements</h2>
you might need atleast a RTX 3060 graphics to have a better inference... especially when running multiple models in the same device, you might need a device which has higher performance. 
