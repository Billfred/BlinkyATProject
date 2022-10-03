# BlinkyATProject
This is a project I'm tackling in the course of my work in the [South Carolina Assistive Technology Program](https://www.sc.edu/study/colleges_schools/medicine/centers_and_institutes_new/center_for_disability_resources/assistive_technology/), part of the University of South Carolina School of Medicine Columbia.

I'll keep the origin story vague for privacy reasons, but the upshot is this: the person that sparked this project needs a pretty big sensory stimulation, but they are also easily upset by most noises and many touch sensations.  Virtually all of our adapted toys rely on either a buzzing motor for motion or a music chip (or both!), so we didn't have a great option.  Light, however, remains an option.

The plan:
* Find an accessibility switch from our collection that's agreeable to them
* 3D print a base for a roughly-tetrahedral set of clear tubes stuffed with NeoPixels -- tetrahedrons should be friendlier to shipping than most other configurations, and we ship items frequently to other parts of the state.
* Use two [NeoSliders](https://www.adafruit.com/product/5295) as adjustments for brightness and animation intensity
* Wire a headphone jack to an IO pin for switch control.  (When I say "headphone jack" I mean a headphone jack, but not for audio--the assistive technology world standardized on 1/8" mono audio connectors for switch connections since they're cheap, pretty widely available, and easy to connect and disconnect.  Check out the [Xbox Adaptive Controller](https://www.xbox.com/en-US/accessories/controllers/xbox-adaptive-controller) for a reference.)
* Use an [Adafruit QT Py RP2040](https://www.adafruit.com/product/4900) for animation and control logic, chosen for a few reasons
  * The STEMMA QT port makes wiring the NeoSliders easy
  * Some of the fancier animations need the extra oomph compared to the standard QT Py for $2.50 less (and even then, I scrapped at least one animation because it bogged down)
  * I'm trying not to introduce new Micro USB things to the world, so the Raspberry Pi Pico is out. (Some of the Chinese knockoffs sporting USB-C are promising, though beyond the scope of this project.)
  * Trying to go through a different vendor to save a buck on the board costs way more in time/shipping/business office work since we're a state agency.
* Mild stretch goal: use the capacitative touch feature to figure out no-switch control.
