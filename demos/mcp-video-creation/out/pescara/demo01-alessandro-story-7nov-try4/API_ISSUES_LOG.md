# API Issues Log

## 2025-11-08 10:00:00 - chirp_tts timeout for Italian story

The `chirp_tts` tool timed out when attempting to synthesize the Italian story (`story-it.txt`). This occurred twice. The text might be too long for a single API call.

## 2025-11-08 10:05:00 - chirp_tts timeout for English story

The `chirp_tts` tool also timed out when attempting to synthesize the English story (`story-en.txt`). This confirms the text is too long for a single API call. I will split the text into smaller chunks for future attempts.

## 2025-11-08 10:10:00 - chirp_tts timeout for single English paragraph

Even a single paragraph from the English story (`Alessandro and the Dragon of Pescara`) timed out when using `chirp_tts`. This indicates a more general issue with the `chirp_tts` tool or the underlying API at this time, rather than just text length. I will pause audio generation and proceed with image generation.

## 2025-11-08 10:20:00 - Audio generation blocked

Due to persistent timeouts with `chirp_tts` even for short texts, audio file generation is currently blocked. I will proceed with other tasks and revisit audio generation later.

## 2025-11-08 10:30:00 - chirp_tts timeout for half Italian story

Attempted to generate audio for half of the Italian story, but `chirp_tts` timed out again. This confirms that the `chirp_tts` tool is currently unusable for any text length. Audio generation is completely blocked.
