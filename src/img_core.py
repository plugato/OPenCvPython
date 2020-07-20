import cv2
import random
import numpy as np
import imutils

def getPossitionTemplate( img_rgb, template ):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    #'Resources/iniciarBatalha.png'

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where( res >= threshold)
    #last_pt = -1
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, (pt[0] + 10, pt[1] +10 ), (pt[0] + w - 10, pt[1] + h - 10 ), (0,0,255), 1)
        last_pt=pt

    try:
        if last_pt:
            a = random.randrange(last_pt[0] + 10, last_pt[0] + w - 10)
            b = random.randrange(last_pt[1] + 10, last_pt[1] + h - 10)

            cv2.line(img_rgb, (a, b), (a, b), (0, 0, 255))
            cv2.circle(img_rgb, (a, b), 10, (255, 255, 0), 5)
            cv2.imshow("img_rgb",img_rgb)
            cv2.waitKey(0)
            print( [a, b ] )
            return [a, b ]
        #os.system(os.getcwd() + '/Resources/nox_adb shell input tap ' + str(a) + ' ' + str(b))


    except NameError:
        return [0, 0]
        last_pt = -1# nope
#if not last_pt:

def multipleResolutionGetPossitionTemplate( img_rgb, template ):

   # template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)

    (tH, tW) = template.shape[:2]
   # cv2.imshow("Template", template)
    # loop over the images to find the template in


    # load the image, convert it to grayscale, and initialize the
    # bookkeeping variable to keep track of the matched region
    image = img_rgb
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    found = None
    # loop over the scales of the image
    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        # resize the image according to the scale, and keep track
        # of the ratio of the resizing
        resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])
        # if the resized image is smaller than the template, then break
        # from the loop
        if resized.shape[0] < tH or resized.shape[1] < tW:
            break
        # detect edges in the resized, grayscale image and apply template
        # matching to find the template in the image
        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        w, h = template.shape[::-1]
        cv2.rectangle(img_rgb, (maxLoc[0] + 10, maxLoc[1] + 10), (maxLoc[0] + w - 10, maxLoc[1] + h - 10), (0, 0, 255), 1)
        last_pt = maxLoc

        try:
            if last_pt:
                a = random.randrange(last_pt[0] + 10, last_pt[0] + w - 10)
                b = random.randrange(last_pt[1] + 10, last_pt[1] + h - 10)

                cv2.line(img_rgb, (a, b), (a, b), (0, 0, 255))
                cv2.circle(img_rgb, (a, b), 10, (255, 255, 0), 5)
        except NameError:
            return [0, 0]
        # check to see if the iteration should be visualized
        if False:
            # draw a bounding box around the detected region
            clone = np.dstack([edged, edged, edged])
            cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                          (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
            #cv2.imshow("Visualize", clone)
            #cv2.waitKey(0)
        # if we have found a new maximum correlation value, then update
        # the bookkeeping variable
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)
    # unpack the bookkeeping variable and compute the (x, y) coordinates
    # of the bounding box based on the resized ratio
    (_, maxLoc, r) = found
    (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
    (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
    # draw a bounding box around the detected result and display the image
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    return [a, b]
