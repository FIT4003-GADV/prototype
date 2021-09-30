import { Box, Typography } from "@mui/material"

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
          intro
        </Typography>
      </Box>
    )
}

export default IntroSection