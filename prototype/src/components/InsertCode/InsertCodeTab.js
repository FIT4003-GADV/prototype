import { Button, Card, CardContent, Grid } from '@mui/material';
import { Form, Formik } from 'formik';
import React from 'react';
import { object, string } from 'yup';
import CodeInput from './CodeInput';

const InsertCodeTab = () => {
  return (
    <Card>
      <CardContent>
        <Formik
          initialValues={{ xmlcode: "" }}
          validationSchema={object({
            xmlcode: string().required(),
          })}
          onSubmit={(values) => {
            console.log('values', values);
            return new Promise((res) => setTimeout(res, 2000));
          }}
        >
          {({ values, errors, isValid, isSubmitting }) => (
            <Form>
              <Grid container spacing={2} direction="column">
                <CodeInput name="xmlcode"/>
                <Grid item>
                  <Button
                    variant="contained"
                    color="primary"
                    disabled={!isValid || isSubmitting}
                    type="submit"
                  >
                    Submit
                  </Button>
                </Grid>
              </Grid>
              <pre>{values && JSON.stringify({ values, errors }, null, 4)}</pre>
            </Form>
          )}
        </Formik>
      </CardContent>
    </Card>
  );
}

export default InsertCodeTab