# Loopback / Audio Midi / Recoding Background / Blackhole

The combination AudioMidi + BlackHole is free of charge. Since the software alternative 'Loopback' is paid, we're going to use the first option instead.

### How Blackhole works

BlackHole has an internal loop, which enables redirecting some audio output to an audio input.

It works as follows:

```
Playing App --> BlackHole Output  ───internal loop───> BlackHole Input --> Recording App
```

As you can see, BlackHole does not “spy” on system audio, processing all sounds. Instead, it captures just the audio stream explicitly sent to the Blackhole interface.

### Recording the Background only

- Select the BlackHole 2ch interface as standard audio input **and** output

### Hearing + Recording the Background

- Create a Multi-Output Device containing the speakers you would like to use + Blackhole 2ch.
- Select the main speaker (e.g. MacBook Pro Speakers) as primary device and set the drift correction to the others.
- 48,0 kHz as sample rate is a good start
- Select this Multi-Output device as the standard audio output **and** the Blackhole interface as the standard input

### Why just creating an 'Aggregate Device' doesn't work

In an aggregate device, you can combine multiple audio devices, containing multiple audio input and output channels. In theory, you couldselect your audio devices intefaces (e.g. MacBook + Edifier speakers) and the black hole into a single aggregate device while multiple channels and use this device as both input and output.

```
Aggregate Device (Virtual Interface)
Ch1 Ch2 = BlackHole
Ch3 Ch4 = MacBook Speakers
Ch5 Ch6 = Edifier Speakers
```

But here's the catch: MacBook just use the **first** 2 channels as outputs. That means, since you need 6 output channels (2 from MacBook + 2 from Edifier + 2 from BlackHole), you can't do it all simultaneously: for instance, if the first two channels belong to the Macbook, only it will output audio neither blackhole nor edifier will be used.

For this reason, you need to create the Multi-Output device, which sends the same audio stream to several output devices simultaneously (fan-out / duplication mechanism), as follows:

```
Multi-Output Device
    L,R
     │
     ├──> BlackHole L,R
     └──> MacBook Speakers L,R
     └──> Edifier Speakers L,R
```

---

I have a MacBook and I would like to use the Audio MIDI setup to – at the same time – while playing some music (1) output a sound through the speakers and (2) input the same music sound through an background virtual interface.

How can I do it?

I created an Aggregate Device interface on Audio MIDI Setup containing both the BlackHole 2ch and the MacBook Pro Speakers:

Subdevice Blackhole 2ch: input channels 1 and 2; output channels 1 and 2;
Subdevice MacBook Pro Speakers: Input channels - (none); output channels 3 and 4.

By doing that, I could successfully record/input the music being played. The problem is: I couldn't hear the output myself through the speakers.

Note: for successfully recording the music I must select this aggregate device as both input and output AND the device speakers MUST BE the Blackhole.
