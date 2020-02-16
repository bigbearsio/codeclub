# Interviewer Guides 

## Prereqs
* Hardware : Microphone
* Software 
   * Audio Hijack
* Permissions & Accounts (Ask P Mhee)
   * GCP Bucket - for podcast upload
   * Ghost - https://codeclub.bigbears.io

## How to Record Interview
1. Dial Facetime with the interviewee
2. Test record for a few seconds and listen to sample. Make sure audio is clear on both side
3. Record

## How to upload
1. Upload file to GCP Bucket
2. https://console.cloud.google.com/storage/browser/codeclub-content?project=codeclub-podcast

```
gsutil cp ~/Music/Audio\ Hijack/EP\ 17\ -\ Phoenix.mp3 gs://codeclub-content/CodeClub-EP17-Phoenix.mp3
```

3. Create a post in ghost
  * tags - 'podcasts'
  * In 'Facebook Cards' add this link `https://codeclub-content.bigbears.io/{FileName}.mp3`
  * Make sure file is MP3 for now
