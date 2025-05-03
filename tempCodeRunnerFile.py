# Evaluate only if original image is provided
                original_image = request.form.get("original_image", "").strip()
                original_text = request.form.get("original_text", "").strip()
                print("hiya")
                
                if original_image and original_text:
                    metrics = text_in_image.evaluate_steganography(original_image, image_path, original_text, decoded_text_path)
                    print("Metrics:", metrics)

                show_metrics_button = True