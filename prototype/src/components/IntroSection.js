import { Box, Typography } from "@material-ui/core"

const IntroSection = () => {
    return(
      <Box marginTop={10}>
        <Typography
          variant="h3"
          align="center"
          color="text.primary"
          gutterBottom
        >
          Album layout
        </Typography>
        <Typography variant="p" align="center" color="text.secondary" paragraph >
          Something short and leading about the collection below—its contents,
          the creator, etc. Make it short and sweet, but not too short so folks
          don&apos;t simply skip over it entirely.
          Something short and leading about the collection below—its contents,
          the creator, etc. Make it short and sweet, but not too short so folks
          don&apos;t simply skip over it entirely.
          Something short and leading about the collection below—its contents,
          the creator, etc. Make it short and sweet, but not too short so folks
          don&apos;t simply skip over it entirely.
          Something short and leading about the collection below—its contents,
          the creator, etc. Make it short and sweet, but not too short so folks
          don&apos;t simply skip over it entirely.
        </Typography>
      </Box>
    )
}

export default IntroSection