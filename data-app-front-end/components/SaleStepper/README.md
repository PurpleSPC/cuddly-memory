# Sale Form Stepper

A comprehensive 3-step stepper component for creating sales with the following stages:

## Steps

### Step 1: Basic Sale Info
- Collects basic sale information including:
  - Sale Date
  - Received Date
  - Account ID
  - Product Line ID
  - Surgeon ID
  - Rep ID
  - Restock Location ID

### Step 2: Sale Items
- Allows users to add/edit sale items
- Features:
  - Product search by catalog # or description
  - Quantity input with validation (0-99)
  - Unit price input
  - Auto-calculated line totals
  - Add/remove items
  - Running total calculation

### Step 3: Review & Submit
- Comprehensive review of all entered information
- Shows summary of basic info and items
- Displays total amount
- Final submission with loading states
- Success confirmation

## Usage

```tsx
import SaleFormStepper from "./components/SaleStepper/SaleFormStepper";

function CreateSalePage() {
    const {
        step,
        setStep,
        saleID,
        basicInfoForm,
    } = useSaleForm();

    return (
        <SaleFormStepper
            step={step}
            setStep={setStep}
            saleID={saleID}
            onSubmitBasicInfo={handleSubmitBasicInfo}
            saleForm={basicInfoForm}
        />
    );
}
```

## Features

- **Visual Step Indicators**: Clear progress indication with step numbers and descriptions
- **Navigation Controls**: Previous/Next buttons with proper state management
- **Form Validation**: Zod schema validation for all inputs
- **Responsive Design**: Mobile-friendly layout with proper spacing
- **State Management**: Integrated with useSaleForm hook for form state
- **Error Handling**: Comprehensive error states and user feedback
- **Loading States**: Proper loading indicators during submissions

## Dependencies

- React 19+
- TypeScript
- Tailwind CSS
- Zod for validation
- Custom form hooks (useForm, useSaleForm)

## Customization

The stepper can be customized by:
- Modifying the step configurations in `SaleFormStepper.tsx`
- Updating the validation schemas in the `schemas/` directory
- Customizing the styling using Tailwind classes
- Extending the form fields and validation rules
