"use client"

import React, { useState } from "react";
import { BasicSaleInfo } from "@/app/schemas/basicSaleInfo";
import { SaleItem } from "@/app/schemas/saleItem";

interface StepReviewProps {
    saleID: number | null;
}

// 3rd final step of SaleFormStepper
export default function StepReview({ saleID }: StepReviewProps) {
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [submissionSuccess, setSubmissionSuccess] = useState(false);
    const [submissionError, setSubmissionError] = useState<string | null>(null);

    // Mock data - in real app this would come from context or props
    const mockBasicInfo: BasicSaleInfo = {
        saleDate: "2024-01-15",
        receivedDate: "2024-01-15",
        accountID: 12345,
        productLineID: 1,
        surgeonID: 67890,
        repID: 11111,
        rstckLocID: 1
    };

    const mockItems: SaleItem[] = [
        { saleID: saleID || 0, productID: 1001, qty: 2, unitPrice: 25.99, lineTotal: 51.98 },
        { saleID: saleID || 0, productID: 1002, qty: 1, unitPrice: 15.50, lineTotal: 15.50 },
        { saleID: saleID || 0, productID: 1003, qty: 3, unitPrice: 8.75, lineTotal: 26.25 }
    ];

    const totalAmount = mockItems.reduce((sum, item) => sum + (item.lineTotal || 0), 0);

    const handleSubmit = async () => {
        setIsSubmitting(true);
        setSubmissionError(null);

        try {
            // Mock API call - replace with actual endpoint
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            // Simulate success
            setSubmissionSuccess(true);
            
            // In real app, you might redirect or show success message
            console.log("Sale submitted successfully!");
            
        } catch (error) {
            setSubmissionError("Failed to submit sale. Please try again.");
            console.error("Submission error:", error);
        } finally {
            setIsSubmitting(false);
        }
    };

    if (submissionSuccess) {
        return (
            <div className="text-center py-12">
                <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                    <svg className="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                </div>
                <h3 className="text-xl font-semibold text-green-800 mb-2">Sale Submitted Successfully!</h3>
                <p className="text-gray-600 mb-4">Your sale has been created and is now in the system.</p>
                <div className="text-sm text-gray-500">
                    Sale ID: <span className="font-mono font-medium">{saleID}</span>
                </div>
            </div>
        );
    }

    return (
        <div className="space-y-6">
            <div className="text-center">
                <h3 className="text-xl font-semibold mb-2">Review Sale Details</h3>
                <p className="text-gray-600">Please review all information before submitting</p>
            </div>

            {/* Basic Info Summary */}
            <div className="bg-gray-50 rounded-lg p-6">
                <h4 className="text-lg font-medium mb-4">Basic Information</h4>
                <div className="grid grid-cols-2 gap-4">
                    <div>
                        <span className="text-sm text-gray-500">Sale Date:</span>
                        <p className="font-medium">{mockBasicInfo.saleDate}</p>
                    </div>
                    <div>
                        <span className="text-sm text-gray-500">Received Date:</span>
                        <p className="font-medium">{mockBasicInfo.receivedDate}</p>
                    </div>
                    <div>
                        <span className="text-sm text-gray-500">Account ID:</span>
                        <p className="font-medium">{mockBasicInfo.accountID}</p>
                    </div>
                    <div>
                        <span className="text-sm text-gray-500">Product Line ID:</span>
                        <p className="font-medium">{mockBasicInfo.productLineID}</p>
                    </div>
                    <div>
                        <span className="text-sm text-gray-500">Surgeon ID:</span>
                        <p className="font-medium">{mockBasicInfo.surgeonID}</p>
                    </div>
                    <div>
                        <span className="text-sm text-gray-500">Rep ID:</span>
                        <p className="font-medium">{mockBasicInfo.repID}</p>
                    </div>
                </div>
            </div>

            {/* Items Summary */}
            <div className="bg-gray-50 rounded-lg p-6">
                <h4 className="text-lg font-medium mb-4">Sale Items</h4>
                <div className="overflow-x-auto">
                    <table className="w-full">
                        <thead>
                            <tr className="border-b border-gray-200">
                                <th className="text-left py-2">Product ID</th>
                                <th className="text-center py-2">Qty</th>
                                <th className="text-center py-2">Unit Price</th>
                                <th className="text-right py-2">Line Total</th>
                            </tr>
                        </thead>
                        <tbody>
                            {mockItems.map((item, index) => (
                                <tr key={index} className="border-b border-gray-100">
                                    <td className="py-2">{item.productID}</td>
                                    <td className="text-center py-2">{item.qty}</td>
                                    <td className="text-center py-2">${item.unitPrice.toFixed(2)}</td>
                                    <td className="text-right py-2 font-medium">${item.lineTotal.toFixed(2)}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
                
                <div className="mt-4 text-right">
                    <div className="text-lg font-semibold">
                        Total Amount: <span className="text-primary">${totalAmount.toFixed(2)}</span>
                    </div>
                </div>
            </div>

            {/* Validation Messages */}
            {submissionError && (
                <div className="bg-red-50 border border-red-200 rounded-lg p-4">
                    <div className="flex">
                        <svg className="w-5 h-5 text-red-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <span className="text-red-800">{submissionError}</span>
                    </div>
                </div>
            )}

            {/* Submit Button */}
            <div className="text-center">
                <button
                    onClick={handleSubmit}
                    disabled={isSubmitting}
                    className={`px-8 py-3 rounded-lg font-medium text-lg transition-colors ${
                        isSubmitting
                            ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                            : 'bg-primary text-white hover:bg-accent'
                    }`}
                >
                    {isSubmitting ? (
                        <div className="flex items-center">
                            <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            Submitting...
                        </div>
                    ) : (
                        'Submit Sale'
                    )}
                </button>
            </div>
        </div>
    );
}