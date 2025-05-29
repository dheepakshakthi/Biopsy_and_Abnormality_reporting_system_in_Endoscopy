# Biopsy_reporting_system_for_Endoscopy

thanks to [datasets.simula.no](https://datasets.simula.no/) for the biopsy instruments dataset <br>dataset available at [datasets.simula.no/kvasir-instrument](https://datasets.simula.no/kvasir-instrument/)

<h2>About the program </h2> 
This program detects the biopsy instruments to check whether the biopsy is being taken or not. <br>
For double biopsy situations, when the first the first biopsy is finished, the instrument is taken away from the camera... it waits for the threshold frames to complete (frames without the biopsy instrument). <br> If the  instrument comes before the camera after the threshold frames, it detects the instrument and reports it as a second biopsy. 
<br><br>

For the detection, i have used [yolo11](https://docs.ultralytics.com/models/yolo11/#supported-tasks-and-modes) and this model is only trained with 250 images due to insufficient favorable data... but it does detect the instruments well. The trained model is available in the "yolo11_instruments_without_pipe_results" under weights folder. 
<br><br>
The kvasir-instruments dataset consisted images of biopsy instruments during biopsy as well as the images of the endoscope pipe. We can confirm the biopsy only when the biopsy instruments are taken out in front of the camera and not the pipe.  
<br>
<h2>Enhancements that can be made</h2>
The biopsy is reported with the location of where the abnormality was seen. Reporting the location can be done with classification of the tract and that can be run side-by-side with this model. (soon to be updated) 
